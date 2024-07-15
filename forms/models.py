from django.db import models
from users.models import User

class WorkCompletionForm(models.Model):
    OMC_CHOICES = [
        ('Goil', 'Goil'),
        ('Vivo', 'Vivo'),
        ('Total', 'Total'),
        ('Others', 'Others'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    omc = models.CharField(max_length=20, choices=OMC_CHOICES)
    time_commenced = models.DateTimeField()
    time_completed = models.DateTimeField()
    duration = models.DurationField()
    material_used = models.CharField(max_length=255)
    quantity = models.IntegerField()
    number_of_workmen = models.IntegerField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    kilometers_traveled = models.DecimalField(max_digits=5, decimal_places=2)
    lost_time_incidents = models.IntegerField(default=0)
    medical_treatment_cases = models.IntegerField(default=0)
    first_aid_cases = models.IntegerField(default=0)
    oil_spilled = models.DecimalField(max_digits=5, decimal_places=2)
    site_comment = models.TextField()
    google_address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='work_completion_images/', null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.duration = self.time_completed - self.time_commenced
        super().save(*args, **kwargs)



class ToolboxTalkForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    talk_date = models.DateField()
    subject = models.CharField(max_length=255)
    details = models.TextField()
    attendees = models.IntegerField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='toolbox_talk_images/', null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
