# Generated by Django 3.2.8 on 2022-03-19 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_buyer', '0003_order_tb'),
        ('site_seller', '0005_auto_20220307_2151'),
    ]

    operations = [
        migrations.CreateModel(
            name='tracking_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_buyer.order_tb')),
            ],
        ),
    ]
