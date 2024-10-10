from django.urls import path
from .views import upload_csv, get_user_data

urlpatterns = [
    path('upload/', upload_csv, name='upload_csv'),
    path('users/', get_user_data, name='get_user_data'),
]