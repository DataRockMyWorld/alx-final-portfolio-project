from django.db import models
from users.models import User

class IncidentReport(models.Model):
    SITE_CHOICES = [
        ('Vivo', 'Vivo'),
        ('Goil', 'Goil'),
        ('Total Energy', 'Total Energy'),
    ]
    INCIDENT_TYPE_CHOICES = [
        ('Potential Incident', 'Potential Incident'),
        ('Near Miss', 'Near Miss'),
    ]
    IMPACT_TYPE_CHOICES = [
        ('Safety', 'Safety'),
        ('Health', 'Health'),
        ('Environment', 'Environment'),
        ('Security', 'Security'),
        ('Reputation', 'Reputation'),
    ]
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Close', 'Close'),
    ]
    site = models.CharField(max_length=20, choices=SITE_CHOICES)
    date_time = models.DateTimeField()
    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPE_CHOICES)
    impact_type = models.CharField(max_length=20, choices=IMPACT_TYPE_CHOICES)
    details = models.TextField()
    location = models.CharField(max_length=255)
    immediate_action = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Open')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

