from django.db import models
 
class Student(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=14,null=True,blank=True)
    location=models.CharField(max_length=255)

    def __str__(self):
        return self.first_name
