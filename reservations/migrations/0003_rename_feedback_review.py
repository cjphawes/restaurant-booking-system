# Generated by Django 4.2.15 on 2024-09-19 13:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservations', '0002_feedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feedback',
            new_name='Review',
        ),
    ]
