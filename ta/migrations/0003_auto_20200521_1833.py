# Generated by Django 3.0.6 on 2020-05-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0007_auto_20200519_1611'),
        ('ta', '0002_ta_classroom_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ta',
            name='l_name',
            field=models.ManyToManyField(to='lecture.Lecture', verbose_name='Lecture name'),
        ),
    ]
