# Generated by Django 4.1.6 on 2023-02-17 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0022_alter_cartitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(default='', upload_to='django-shop/groceryStore/img/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='', upload_to='django-shop/groceryStore/img/'),
        ),
    ]
