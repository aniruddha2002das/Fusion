# Generated by Django 3.1.5 on 2024-02-17 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0001_initial'),
        ('hostel_management', '0003_hall_assigned_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelallotment',
            name='assignedCaretaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.staff'),
        ),
        migrations.AlterField(
            model_name='hostelallotment',
            name='assignedWarden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.faculty'),
        ),
    ]
