# Generated by Django 4.2.6 on 2023-11-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_remove_order_order_item_order_order_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_item',
            field=models.ManyToManyField(to='store.product'),
        ),
    ]