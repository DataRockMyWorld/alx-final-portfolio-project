from django.db import models
from django.utils import timezone
from users.models import User

class KPI(models.Model):
    CATEGORY_CHOICES = [
        ('Leading Indicators', 'Leading Indicators'),
        ('Lagging Indicators', 'Lagging Indicators'),
        ('Incident Rates', 'Incident Rates'),
    ]
    
    OBJECTIVES = [
        ("Improve Control of Work (Cow)", "Improve Control of Work (Cow)"),
        ("Improve Behaviour Based Safety and Culture","Improve Behaviour Based Safety and Culture"),
        ("Maintain Workplace Controls","Maintain Workplace Controls"),
        ("Improve Emergency Response","Improve Emergency Response"),
        ("Comply with Legal Requirements)","Comply with Legal Requirements)"),
        ("Protect life, Property and Environment","Protect life, Property and Environment"),
        ("Reduce Incident Rates","Reduce Incident Rates"),
        ("Continually improve the HSSE Management System","Continually improve the HSSE Management System"),
    ]
    Objective = models.CharField(max_length=255, choices=OBJECTIVES, default="Improve Control of Work (Cow)")
    kpi_name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    actual_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    target_value = models.DecimalField(max_digits=10, decimal_places=2)
    
    def percentage_achieved(self):
        if self.target_value == 0:
            return 0
        return round((self.actual_value / self.target_value) * 100, 2)


    def __str__(self):
        return self.kpi_name
