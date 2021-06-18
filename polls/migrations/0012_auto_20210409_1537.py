# Generated by Django 3.1.7 on 2021-04-09 12:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20210409_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 9, 12, 37, 53, 416798, tzinfo=utc), verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]