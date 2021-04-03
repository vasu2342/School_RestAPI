from django.db import models


class Student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=64)
    sclass=models.CharField(max_length=64)

class Teacher(models.Model):
    student=models.ForeignKey(Student, related_name='tracks', on_delete=models.CASCADE)
    smarks=models.IntegerField()
    spercentage=models.CharField(max_length=64)
    

# Create your models here.
