# Generated by Django 3.1.1 on 2020-09-18 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
