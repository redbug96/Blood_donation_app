from django.db import models


# Create your models here.
class Donor(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=20)
    Blood_group = models.CharField(max_length=10)
    District = models.CharField(max_length=20)
    Mobile_number = models.CharField(max_length=13)
    Mail_id = models.EmailField(max_length=50)
    Photo = models.FileField()
    Health_issue = models.CharField(max_length=255)
    Username=models.CharField(max_length=255)
    Password=models.CharField(max_length=255)
    Validation=models.BooleanField(default=False,null=True)



class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.IntegerField(default=0)

class Request_donor(models.Model):
    donor_id=models.IntegerField()
    status=models.IntegerField(default=0)
