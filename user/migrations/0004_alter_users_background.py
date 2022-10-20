# Generated by Django 4.1.2 on 2022-10-20 18:05

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_users_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='background',
            field=models.ImageField(default='background/big-sur-4k-wp.jpg', null=True, upload_to=user.models.Users.date_upload_to_bg),
        ),
    ]
