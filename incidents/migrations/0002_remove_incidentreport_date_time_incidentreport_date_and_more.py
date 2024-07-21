# Generated by Django 4.2.14 on 2024-07-18 14:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("incidents", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="incidentreport",
            name="date_time",
        ),
        migrations.AddField(
            model_name="incidentreport",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="incidentreport",
            name="time",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]