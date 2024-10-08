# Generated by Django 5.0.6 on 2024-10-03 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_order_seller_orderitem_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=10, null=True),
        ),
    ]
