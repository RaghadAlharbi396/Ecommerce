# Generated by Django 4.2.6 on 2023-11-13 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_basket_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='store.basket'),
        ),
    ]