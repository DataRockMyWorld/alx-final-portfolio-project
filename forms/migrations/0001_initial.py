# Generated by Django 4.2.14 on 2024-07-10 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkCompletionForm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "omc",
                    models.CharField(
                        choices=[
                            ("Goil", "Goil"),
                            ("Vivo", "Vivo"),
                            ("Total", "Total"),
                            ("Others", "Others"),
                        ],
                        max_length=20,
                    ),
                ),
                ("time_commenced", models.DateTimeField()),
                ("time_completed", models.DateTimeField()),
                ("duration", models.DurationField()),
                ("material_used", models.CharField(max_length=255)),
                ("quantity", models.IntegerField()),
                ("number_of_workmen", models.IntegerField()),
                ("hours_worked", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "kilometers_traveled",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                ("lost_time_incidents", models.IntegerField()),
                ("medical_treatment_cases", models.IntegerField()),
                ("first_aid_cases", models.IntegerField()),
                ("oil_spilled", models.DecimalField(decimal_places=2, max_digits=5)),
                ("site_comment", models.TextField()),
                ("google_address", models.CharField(max_length=255)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
