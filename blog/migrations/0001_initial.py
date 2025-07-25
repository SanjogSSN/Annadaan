# Generated by Django 3.1.6 on 2021-04-14 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation_Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtype', models.CharField(blank=True, choices=[('direct_donation', 'Direct Donation'), ('food_bank', 'Food Bank')], max_length=20)),
                ('time', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('human', models.PositiveSmallIntegerField(max_length=3)),
                ('animal', models.PositiveSmallIntegerField(max_length=3)),
                ('pics', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.BigIntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Food_Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField(max_length=10)),
                ('location', models.CharField(max_length=100)),
                ('incharge', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Food_Bank_Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pics', models.ImageField(upload_to='')),
                ('remark', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Onsite_Processing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_time', models.DateTimeField()),
                ('pickup_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.BigIntegerField(max_length=10)),
                ('food_item', models.CharField(max_length=50)),
                ('quantity', models.PositiveSmallIntegerField(max_length=3)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.BigIntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer_Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('human', models.PositiveSmallIntegerField(max_length=3)),
                ('animal', models.PositiveSmallIntegerField(max_length=3)),
                ('pics', models.ImageField(upload_to='')),
            ],
        ),
    ]
