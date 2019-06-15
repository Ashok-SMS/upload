from django.db import models

# Create your models here.


class Student(models.Model):
    rno = models.BigIntegerField()
    sname = models.CharField(max_length=25)
    category = models.CharField(max_length=20)
    city = models.CharField(max_length=25)
    result = models.CharField(max_length=10)
    # photo = models.ImageField()
