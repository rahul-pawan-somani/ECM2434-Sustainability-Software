# Generated by Django 5.1.6 on 2025-03-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envapp', '0002_alter_stationusers_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='fuelRemaining',
            field=models.IntegerField(default=0),
        ),
    ]
