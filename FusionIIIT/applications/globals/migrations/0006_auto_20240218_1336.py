# Generated by Django 3.1.5 on 2024-02-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0005_auto_20240218_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='user_status',
            field=models.CharField(choices=[('NEW', 'NEW'), ('PRESENT', 'PRESENT')], default='PRESENT', max_length=50),
        ),
    ]
