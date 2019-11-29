from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    email = models.EmailField()
    DOB = models.DateTimeField()
    def __str__(self):
        return f'Full Name : {self.firstname}  {self.lastname} '
