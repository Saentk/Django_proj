# Generated by Django 3.1.7 on 2021-04-13 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20210413_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='pub_date',
        ),
    ]
