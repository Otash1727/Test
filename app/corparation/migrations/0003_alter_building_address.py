# Generated by Django 5.1.6 on 2025-02-10 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corparation', '0002_remove_building_latidute_building_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='address',
            field=models.CharField(max_length=280, verbose_name='address'),
        ),
    ]
