# Generated by Django 3.1.1 on 2021-02-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0004_auto_20200918_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
