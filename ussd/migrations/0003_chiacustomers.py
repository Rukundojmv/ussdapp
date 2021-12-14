# Generated by Django 3.2.9 on 2021-12-14 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0002_iteganyagihe'),
    ]

    operations = [
        migrations.CreateModel(
            name='chiaCustomers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNumber', models.CharField(max_length=255)),
                ('fullName', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('purchasedTime', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
