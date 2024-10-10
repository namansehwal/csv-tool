from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from .models import UserData
from .serializers import UserDataSerializer
from .utils import data_cleaning

@api_view(['POST'])
def upload_csv(request):
    if 'file' not in request.FILES:
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

    csv_file = request.FILES['file']
    file_path = default_storage.save(f'tmp/{csv_file.name}', csv_file)

    try:
        cleaned_data = data_cleaning.clean(file_path)
        
        # Iterate over the cleaned data and save each row into the database using the serializer
        for index, row in cleaned_data.iterrows():
            data = {
                'name': row['Name'],
                'class_name': row['Class'],
                'school': row['School'],
                'state': row['State']
            }
            serializer = UserDataSerializer(data=data)
            if serializer.is_valid():
                serializer.save()  # Save the data to the database
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
             
        return Response({'message': 'CSV uploaded and processed successfully!'}, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_user_data(request):
    users = UserData.objects.all()
    serializedData = UserDataSerializer(users, many=True).data
    return Response(serializedData)
