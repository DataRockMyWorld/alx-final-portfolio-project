from django.db import models
from users.models import User

class Document(models.Model):
    CATEGORY_CHOICES = [
        ('Form-or-Template', 'Form-or-Template'),
        ('Policy', 'Policy'),
        ('Operational Controls Procedure', 'Operational Controls Procedure'),
        ('System documents', 'System documents'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title