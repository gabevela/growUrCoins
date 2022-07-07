# Generated by Django 4.0.4 on 2022-07-06 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='street_name',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='street_number',
        ),
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.CharField(max_length=200),
        ),
    ]
