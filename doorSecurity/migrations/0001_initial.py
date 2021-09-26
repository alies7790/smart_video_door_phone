# Generated by Django 3.2.6 on 2021-09-25 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rassperypiInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_created=True)),
                ('title_member', models.CharField(max_length=20)),
                ('change_status', models.DateTimeField(auto_now_add=True)),
                ('allow_status', models.IntegerField(choices=[(1, 'فرد اجازه ورود دارد'), (2, 'فرد اجازه ورود ندارد')], default=1, verbose_name='وضعیت دسترسی فرد')),
                ('rassperySystem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rassperypiInfo.rassperysystem')),
            ],
            options={
                'verbose_name': 'مدیریت افراد برای باز شدن درب',
                'verbose_name_plural': 'مدیریت افراد برای باز شدن درب',
            },
        ),
        migrations.CreateModel(
            name='LicenseToUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_lincense', models.DateField(auto_created=True)),
                ('end_lincense', models.DateField()),
                ('rassperypiInfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rassperypiInfo.rassperysystem')),
            ],
            options={
                'verbose_name': 'مدیریت lincense بازکردن در',
                'verbose_name_plural': 'مدیریت lincense بازکردن در',
            },
        ),
        migrations.CreateModel(
            name='HistoryOpenDoor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True)),
                ('request_status', models.IntegerField(choices=[(1, 'در برای فرد باز شد'), (2, 'اجازه برای بازکردن در برای فرد وجود ندارد'), (3, 'همچین شخصی تعریف نشده است')], default=1, verbose_name='وضعیت درخواست')),
                ('rassperypiInfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rassperypiInfo.rassperysystem')),
            ],
            options={
                'verbose_name': 'مدیریت تاریخچه درخواست درب بازشدن',
                'verbose_name_plural': 'مدیریت تاریخچه درخواست درب بازشدن',
            },
        ),
    ]