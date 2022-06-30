# Generated by Django 4.0.4 on 2022-06-25 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_title', models.CharField(max_length=15)),
                ('coins', models.IntegerField()),
                ('description', models.TextField(max_length=250)),
                ('offer_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('stock_inventory', models.IntegerField()),
                ('picture_one', models.URLField()),
                ('category', models.CharField(max_length=100)),
                ('street_number', models.CharField(max_length=100)),
                ('street_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.IntegerField()),
                ('feedback', models.TextField(max_length=250)),
            ],
        ),
    ]