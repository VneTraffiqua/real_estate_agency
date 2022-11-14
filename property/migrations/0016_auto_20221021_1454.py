from django.db import transaction
from django.db import migrations


def fill_owners_fields(apps, schema_editor):
    flats_db = apps.get_model('property', 'Flat')
    owners_db = apps.get_model('property', 'Owner')
    flats = flats_db.objects.all()
    for flat in flats:
        with transaction.atomic():
            flat.owners_flats.get_or_create(
                owner=flat.owner,
                owners_phonenumber=flat.owners_phonenumber,
                owner_pure_phone=flat.owner_pure_phone
            )


def fill_owners_fields_backward(apps, schema_editor):
    owners_db = apps.get_model('property', 'Owner')
    owners_db.objects.all().update(
        owner=None,
        owners_phonenumber=None,
        owner_pure_phone=None
    )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_owner'),
    ]

    operations = [
        migrations.RunPython(
            fill_owners_fields, fill_owners_fields_backward
        )
    ]
