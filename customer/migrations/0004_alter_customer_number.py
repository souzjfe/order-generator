# Generated by Django 4.2.3 on 2024-07-16 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customer_cpf_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='number',
            field=models.IntegerField(blank=True, default=0, verbose_name='Número'),
        ),
    ]
