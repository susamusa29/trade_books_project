# Generated by Django 2.2.3 on 2020-03-20 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tradebooks', '0007_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='paymentID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='book_payment', to='tradebooks.UserProfile'),
        ),
    ]
