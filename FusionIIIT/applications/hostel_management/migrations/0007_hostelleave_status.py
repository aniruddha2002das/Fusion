# Generated by Django 3.1.5 on 2024-02-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_management', '0006_remove_hostelcomplaint_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostelleave',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
