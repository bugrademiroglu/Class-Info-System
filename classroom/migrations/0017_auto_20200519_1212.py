# Generated by Django 3.0.6 on 2020-05-19 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0006_remove_lecture_classroom_name'),
        ('classroom', '0016_auto_20200519_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='l_name',
            field=models.ManyToManyField(to='lecture.Lecture', verbose_name='Classroom'),
        ),
    ]
