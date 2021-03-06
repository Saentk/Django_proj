# Generated by Django 3.1.7 on 2021-04-08 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20210405_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.AlterField(
            model_name='info',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date published'),
        ),
    ]
