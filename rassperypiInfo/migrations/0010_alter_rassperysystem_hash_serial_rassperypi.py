# Generated by Django 3.2.7 on 2021-11-04 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rassperypiInfo', '0009_rename_token_rassperysystem_token_connect_rassperypi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rassperysystem',
            name='hash_serial_rassperyPi',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='hash سریال رزپری پای'),
        ),
    ]