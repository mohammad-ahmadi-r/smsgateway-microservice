# Generated by Django 4.2.6 on 2023-10-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]