# Generated by Django 4.2.15 on 2024-08-12 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0006_alter_customer_first_name_alter_customer_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
    ]
