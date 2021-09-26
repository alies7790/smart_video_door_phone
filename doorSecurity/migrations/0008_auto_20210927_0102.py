# Generated by Django 3.2.7 on 2021-09-27 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doorSecurity', '0007_auto_20210926_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='title_member',
            new_name='name',
        ),
        migrations.AddField(
            model_name='members',
            name='title',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
