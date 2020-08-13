from django.db import models

# Create your models here.
class Student (models.Model) :
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=60, default='default vaule')
    lastName = models.CharField(max_length=60, default='default vaule')
    userId = models.IntegerField()

    def __int__(self) :
        return self.id