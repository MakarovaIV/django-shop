# Generated by Django 4.1.6 on 2023-02-13 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, max_length=500)),
                ('composition', models.CharField(blank=True, max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('units', models.CharField(max_length=10)),
                ('picture', models.ImageField(default='', upload_to='img')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.category')),
            ],
        ),
    ]
