from django.db import models
from  django.contrib.auth.models import User


class Attendance(models.Model):
    name = models.CharField(max_length=30)
    candidate_id = models.IntegerField()
    Candidate_Attendance = models.IntegerField(default = 1)
    def __str__(self):
        return self.name

class Login(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    Img = models.ImageField(upload_to='images/',blank = True,null = True)
    def __str__(self):
        return self.email


class SignUp(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    def __str__(self):
        return self.email

