# Generated by Django 3.2 on 2022-12-02 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0020_auto_20221201_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='owner',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='flat_complaint',
        ),
        migrations.AddField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(
                blank=True,
                default='',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='complaints',
                to='property.flat',
                verbose_name='Квартира, на которую пожаловались'
            ),
            preserve_default=False,
        ),
    ]
