# Generated by Django 4.2.3 on 2024-07-16 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_monthly_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='down_payment_percentage',
        ),
    ]
