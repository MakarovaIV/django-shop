# Generated by Django 4.1.6 on 2023-02-15 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0015_remove_order_cart_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=2),
        ),
    ]
