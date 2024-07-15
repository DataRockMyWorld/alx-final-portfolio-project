from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    DEPARTMENT_CHOICES = [
        ('Operations', 'Operations'),
        ('Finance', 'Finance'),
        ('Stores', 'Stores'),
        ('HSSE', 'HSSE'),
        ('MD', 'MD'),
    ]
    
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    
