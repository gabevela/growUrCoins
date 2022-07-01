from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_ad_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='expiry_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ad',
            name='offer_date',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.ad')),
            ],
        ),
    ]
