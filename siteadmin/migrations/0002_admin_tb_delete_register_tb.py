# Generated by Django 4.2.3 on 2023-08-06 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userame', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Register_tb',
        ),
    ]
