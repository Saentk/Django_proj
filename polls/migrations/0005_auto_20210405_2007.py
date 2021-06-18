# Generated by Django 3.1.7 on 2021-04-05 17:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210405_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_title', models.CharField(max_length=200, verbose_name='Info_name')),
                ('info_text', models.TextField(verbose_name='Text')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 4, 5, 17, 7, 13, 670777, tzinfo=utc), verbose_name='Date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Informati',
        ),
    ]