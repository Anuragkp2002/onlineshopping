# Generated by Django 4.2.3 on 2023-08-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0003_rename_userame_admin_tb_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='category_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=20)),
            ],
        ),
    ]