# Generated by Django 3.0.5 on 2020-04-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_auto_20200419_2147'),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='ads_name',
            field=models.CharField(max_length=50, verbose_name='Ad Name'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='dep_name',
            field=models.ManyToManyField(to='department.Department', verbose_name='Department Name'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='image_ads',
            field=models.FileField(blank=True, upload_to='image', verbose_name='Image of Ad'),
        ),
    ]