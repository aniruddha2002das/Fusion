# Generated by Django 3.1.5 on 2024-02-17 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0002_auto_20240217_1949'),
        ('hostel_management', '0004_auto_20240217_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelallotment',
            name='assignedCaretaker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.staff'),
        ),
        migrations.AlterField(
            model_name='hostelallotment',
            name='assignedWarden',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.faculty'),
        ),
    ]
