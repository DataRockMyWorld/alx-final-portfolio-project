from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class User(AbstractUser):
    DEPARTMENT_CHOICES = [
        ('Operations', 'Operations'),
        ('Finance', 'Finance'),
        ('Stores', 'Stores'),
        ('HSSE', 'HSSE'),
        ('MD', 'MD'),
    ]
    
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    is_approved = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    