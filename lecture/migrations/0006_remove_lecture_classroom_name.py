# Generated by Django 3.0.6 on 2020-05-18 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0005_auto_20200518_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='classroom_name',
        ),
    ]