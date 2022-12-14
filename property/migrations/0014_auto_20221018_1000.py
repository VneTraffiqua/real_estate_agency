# Generated by Django 2.2.24 on 2022-10-18 07:00
import phonenumbers
from django.db import migrations


def get_owner_pure_phone(apps, schema_editor):
    flats_db = apps.get_model('property', 'Flat')
    flats = flats_db.objects.all()
    for flat in flats.iterator():
        owner_pure_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if not phonenumbers.is_valid_number(owner_pure_phone):
            continue
        flat.pure_phone = owner_pure_phone
        flat.save()


def owner_pure_phone_backward(apps, schema_editor):
    flats_db = apps.get_model('property', 'Flat')
    flats_db.objects.all().update(owner_pure_phone=None)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20221018_0938'),
    ]

    operations = [
        migrations.RunPython(
            get_owner_pure_phone, owner_pure_phone_backward
        )
    ]
