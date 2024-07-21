# Generated by Django 4.2.14 on 2024-07-18 14:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0004_workcompletionform_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="toolboxtalkform",
            old_name="location",
            new_name="site_name",
        ),
        migrations.RemoveField(
            model_name="toolboxtalkform",
            name="details",
        ),
        migrations.RemoveField(
            model_name="toolboxtalkform",
            name="subject",
        ),
        migrations.RemoveField(
            model_name="toolboxtalkform",
            name="talk_date",
        ),
        migrations.AddField(
            model_name="toolboxtalkform",
            name="Job_description",
            field=models.CharField(
                choices=[
                    ("Corrective", "Corrective"),
                    ("Preventive", "Preventive"),
                    ("Installation", "Installation"),
                    ("Bolting", "Bolting"),
                ],
                default="Corrective",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="toolboxtalkform",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="toolboxtalkform",
            name="omc",
            field=models.CharField(
                choices=[
                    ("Goil", "Goil"),
                    ("Vivo", "Vivo"),
                    ("Total", "Total"),
                    ("Others", "Others"),
                ],
                default="Goil",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="workcompletionform",
            name="fire_incident",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="workcompletionform",
            name="omc",
            field=models.CharField(
                choices=[
                    ("Goil", "Goil"),
                    ("Vivo", "Vivo"),
                    ("Total", "Total"),
                    ("Others", "Others"),
                ],
                default="Goil",
                max_length=20,
            ),
        ),
    ]