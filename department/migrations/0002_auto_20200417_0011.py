# Generated by Django 3.0.5 on 2020-04-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='d_name',
            field=models.CharField(max_length=50, verbose_name='Department'),
        ),
    ]
