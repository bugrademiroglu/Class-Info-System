# Generated by Django 3.0.5 on 2020-04-21 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200419_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='image_events',
            field=models.ImageField(blank=True, upload_to='image', verbose_name='Picture of Event'),
        ),
    ]