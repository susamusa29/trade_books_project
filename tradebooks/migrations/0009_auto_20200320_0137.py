# Generated by Django 2.2.3 on 2020-03-20 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tradebooks', '0008_book_paymentid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='paymentID',
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('paymentID', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('processed', models.BooleanField(default=False)),
                ('payee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_payee', to='tradebooks.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='payID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tradebooks.Payment'),
        ),
    ]
