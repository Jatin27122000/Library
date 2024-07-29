from django.db import models
from django.contrib.auth.models import User


class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(max_length=254, null=True)
    address = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    active = models.BooleanField(default=True) 

    def __str__(self):
        return self.name
    
