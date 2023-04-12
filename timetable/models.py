from django.db import models

# Create your models here.
class Sem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    department=models.CharField(max_length=255)

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    code=models.CharField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    teaching_hour=models.IntegerField()
    sem = models.ForeignKey(Sem,on_delete=models.CASCADE)
    is_lab = models.BooleanField(default=False)
    uid= models.CharField(max_length=255)
    faculty= models.CharField(max_length=255)


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    is_lab = models.BooleanField(default=False)

class Time(models.Model):
    id = models.AutoField(primary_key=True)
    start=models.CharField(max_length=15)
    end=models.CharField(max_length=15)