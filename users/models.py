from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=250)
    eamil = models.EmailField()
    father_name =models.CharField(max_length=250)

   