# Generated by Django 4.1.6 on 2023-02-14 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0008_alter_cartitem_cart_alter_cartitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
    ]