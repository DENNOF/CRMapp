# Generated by Django 4.2.3 on 2023-07-08 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_inventory_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
                ('Department', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='inventory',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
