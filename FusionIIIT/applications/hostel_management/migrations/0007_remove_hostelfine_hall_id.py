# Generated by Django 3.1.5 on 2024-02-19 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_management', '0006_hostelfine_hall_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostelfine',
            name='hall_id',
        ),
    ]
