# Generated by Django 3.1.6 on 2021-04-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210415_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='volunteer_report',
            name='animal',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='volunteer_report',
            name='human',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
