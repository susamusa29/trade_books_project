# Generated by Django 2.2.3 on 2020-04-01 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradebooks', '0016_auto_20200401_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
    ]
