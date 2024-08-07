# Generated by Django 4.2.14 on 2024-07-17 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_profile_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="profile_image",
        ),
        migrations.AddField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile_pictures/"
            ),
        ),
    ]
