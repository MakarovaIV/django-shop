# Generated by Django 4.1.6 on 2023-02-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0010_cartitem_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='count',
            field=models.IntegerField(null=True),
        ),
    ]
