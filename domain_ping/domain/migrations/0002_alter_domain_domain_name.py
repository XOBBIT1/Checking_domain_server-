# Generated by Django 4.2.4 on 2023-08-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='domain_name',
            field=models.CharField(max_length=200, verbose_name='Ping'),
        ),
    ]
