# Generated by Django 3.1.1 on 2020-09-18 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0002_auto_20200918_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
