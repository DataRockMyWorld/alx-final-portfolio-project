from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    DEPARTMENT_CHOICES = [
        ('Operations', 'Operations'),
        ('Finance', 'Finance'),
        ('HSSE', 'HSSE'),
        ('MDA', 'MDA'),
    ]
    
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    is_approved = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
