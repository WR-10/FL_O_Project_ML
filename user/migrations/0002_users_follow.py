# Generated by Django 4.1.2 on 2022-10-20 06:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='follow',
            field=models.ManyToManyField(related_name='followed', to=settings.AUTH_USER_MODEL),
        ),
    ]
