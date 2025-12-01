from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, default=None)
    price = models.CharField(max_length=100, null=True, blank=True, default=None)
    description = models.CharField(max_length=300, null=True, blank=True, default=None)
    

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="details", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=".", null=True, blank=True, default=None)
    bio = models.TextField(null=True, default=None)
    phone_number = models.CharField(max_length=15, null=True, default=None)
    
    def __str__(self):
        return f"{self.name} {self.price}"
    
    
