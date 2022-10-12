# Generated by Django 2.2.24 on 2022-10-12 07:29

from django.db import migrations


def fill_data_field_new_building(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    flats.objects.filter(construction_year__lt=2015).update(new_building=False)
    flats.objects.filter(construction_year__gt=2014).update(new_building=True)


def fill_data_field_backward(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    flats.objects.all().update(new_building=None)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(
            fill_data_field_new_building, fill_data_field_backward
        )
    ]