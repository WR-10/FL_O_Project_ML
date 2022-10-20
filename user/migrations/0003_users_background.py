# Generated by Django 4.1.2 on 2022-10-20 17:09

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_users_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='background',
            field=models.ImageField(default='background/default_profile.png', null=True, upload_to=user.models.Users.date_upload_to),
        ),
    ]