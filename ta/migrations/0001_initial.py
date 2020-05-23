# Generated by Django 3.0.6 on 2020-05-21 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lecture', '0007_auto_20200519_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='TA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ta_name', models.CharField(max_length=50, unique=True, verbose_name='Teacher Name')),
                ('ta_bdate', models.DateTimeField()),
                ('image_events', models.ImageField(blank=True, upload_to='image', verbose_name='Picture of Lecturer')),
                ('l_name', models.ManyToManyField(to='lecture.Lecture', verbose_name='Lecture Name')),
            ],
        ),
    ]
