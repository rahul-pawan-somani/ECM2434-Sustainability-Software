# Generated by Django 5.1.6 on 2025-03-18 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stationusers',
            options={'ordering': ['-fillTime']},
        ),
    ]
