# Generated by Django 3.1.6 on 2021-05-06 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_delete_food_bank_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation_process',
            name='pics',
        ),
    ]
