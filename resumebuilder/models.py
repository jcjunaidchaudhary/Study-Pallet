from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PersonalInformation(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=255,null=True)
    gender=models.CharField(max_length=10)
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=200)
    marital_status=models.CharField(max_length=10)
    date_of_birth=models.CharField(max_length=20)
    profession=models.CharField(max_length=300)
    objective=models.TextField(max_length=300)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    country=models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user}'
    
    
class WorkExperience(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=300)
    location=models.CharField(max_length=300)
    joining_date=models.CharField(max_length=500)
    end_date=models.CharField(max_length=500)
    designation=models.CharField(max_length=300)
    working_on=models.CharField(max_length=300)
    
    
    def __str__(self) -> str:
        return f'{self.user}'


class Educations(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    institute=models.CharField(max_length=255)
    education=models.CharField(max_length=255)
    passing_year=models.CharField(max_length=500)
    score=models.FloatField()


    def __str__(self):
        return f'{self.user}'

class additionalinfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    skill=models.TextField(max_length=300)
    language=models.CharField(max_length=255)
    personal_wl=models.URLField(max_length=300,null=True)
    
    def __str__(self):
        return f'{self.user}'

class Projects(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField(max_length=255)

    def __str__(self):
        return f'{self.user}'
    
    
class Social_Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    social_profile=models.CharField(max_length=255)
    url=models.URLField(max_length=255)
    
    def __str__(self):
        return f'{self.user}'

        
