# Generated by Django 4.1.6 on 2023-02-15 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0016_alter_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=500),
        ),
    ]
