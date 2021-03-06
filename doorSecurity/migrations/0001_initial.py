# Generated by Django 3.2.7 on 2021-10-04 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rassperypiInfo', '0004_remove_rassperysystem_serial_reset_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('change_status_date', models.DateTimeField(auto_now=True)),
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
                ('start_lincense', models.DateField(auto_now_add=True)),
                ('end_lincense', models.DateField()),
                ('rassperypiInfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rassperypiInfo.rassperysystem')),
            ],
            options={
                'verbose_name': 'مدیریت lincense بازکردن در',
                'verbose_name_plural': 'مدیریت lincense بازکردن در',
            },
        ),
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('request_status', models.IntegerField(choices=[(1, 'در برای فرد باز شد'), (2, 'اجازه برای بازکردن در برای فرد وجود ندارد'), (3, 'همچین شخصی تعریف نشده است')], default=1, verbose_name='وضعیت درخواست')),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doorSecurity.members')),
                ('rassperypiInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rassperypiInfo.rassperysystem')),
            ],
            options={
                'verbose_name': 'مدیریت تاریخچه درخواست درب بازشدن',
                'verbose_name_plural': 'مدیریت تاریخچه درخواست درب بازشدن',
            },
        ),
    ]
