# Generated by Django 2.2.24 on 2022-10-07 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='new_building',
        ),
    ]
