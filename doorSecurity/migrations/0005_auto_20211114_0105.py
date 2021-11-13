# Generated by Django 3.2.7 on 2021-11-14 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doorSecurity', '0004_members_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationservice',
            name='title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='members',
            name='picture',
            field=models.TextField(verbose_name='عکس شخص'),
        ),
    ]
