# Generated by Django 4.2.15 on 2024-08-12 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_alter_reservation_options_alter_reservation_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='username',
        ),
    ]
