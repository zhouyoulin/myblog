from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    birth = models.DateTimeField(blank=True)
    phone = models.CharField(max_length=20,blank=True)