# Generated by Django 3.2.9 on 2021-12-14 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0004_rename_chiacustomers_chiacustomer'),
    ]

    operations = [
        migrations.AddField(
            model_name='chiacustomer',
            name='serviceCode',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chiacustomer',
            name='sessionId',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
