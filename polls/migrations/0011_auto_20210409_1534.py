# Generated by Django 3.1.7 on 2021-04-09 12:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20210408_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images')),
                ('text', models.TextField(verbose_name='Text')),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 9, 12, 34, 32, 132833, tzinfo=utc), verbose_name='Date published'),
        ),
    ]
