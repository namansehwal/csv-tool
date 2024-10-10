from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)  # 'class' is a reserved keyword in Python, so using 'class_name'
    school = models.CharField(max_length=100)
    state = models.CharField(max_length=100)  # Assuming a two-letter state code like 'MA' or 'CA'

    def __str__(self):
        return f'{self.name} - {self.class_name} - {self.school} - {self.state}'
