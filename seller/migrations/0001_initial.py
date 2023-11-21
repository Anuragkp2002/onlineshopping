# Generated by Django 4.2.3 on 2023-08-09 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sellerregister_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=20)),
                ('DOB', models.CharField(max_length=20)),
                ('Phonenumber', models.CharField(max_length=20)),
                ('Country', models.CharField(max_length=20)),
                ('File', models.CharField(max_length=20)),
                ('Username', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('Status', models.CharField(default='pending', max_length=20)),
            ],
        ),
    ]
