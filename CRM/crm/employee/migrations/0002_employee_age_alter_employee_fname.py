# Generated by Django 4.2.3 on 2023-07-08 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.CharField(default='hes', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Fname',
            field=models.CharField(default='hd', max_length=20),
        ),
    ]
