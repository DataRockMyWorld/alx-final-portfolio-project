# Generated by Django 4.2.14 on 2024-07-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "incidents",
            "0002_remove_incidentreport_date_time_incidentreport_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="incidentreport",
            name="incident_number",
            field=models.IntegerField(default=1),
        ),
    ]