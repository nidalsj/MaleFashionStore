# Generated by Django 5.0.6 on 2024-06-23 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_rename_name_customer_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
    ]
