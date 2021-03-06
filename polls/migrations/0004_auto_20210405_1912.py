# Generated by Django 3.1.7 on 2021-04-05 16:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_informati'),
    ]

    operations = [
        migrations.AddField(
            model_name='informati',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 5, 16, 12, 20, 589410, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
