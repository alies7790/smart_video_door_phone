# Generated by Django 3.2.7 on 2021-11-04 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rassperypiInfo', '0008_alter_rassperysystem_hash_serial_rassperypi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rassperysystem',
            old_name='token',
            new_name='token_connect_rassperypi',
        ),
    ]
