# Generated by Django 4.2.3 on 2023-08-22 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0007_payment_tb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment_tb',
            old_name='Expirtdate',
            new_name='Expirydate',
        ),
    ]