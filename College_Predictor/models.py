from django.db import models

# Create your models here.
class College(models.Model):
    college_Name=models.CharField(max_length=100)
    college_ID=models.CharField(max_length=10)
    location=models.CharField(max_length=100)
    rank=models.BigIntegerField()
    category=models.CharField(max_length=20)
    branch=models.CharField(max_length=100)
    about=models.CharField(max_length=100)

    def __str__(self):
        return self.college_Name



