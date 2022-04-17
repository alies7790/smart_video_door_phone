from django.db import models

# Create your models here.
from accounts.models import Profiles
from rassperypiInfo.models import RassperySystem




class InformationService(models.Model):
    class Meta:
        verbose_name= 'مدیریت اطلاعات سرویس'
        verbose_name_plural= 'مدیریت اطلاعات سرویس'
    rassperypiInfo = models.OneToOneField(RassperySystem, on_delete=models.CASCADE)
    lincense=models.OneToOneField('LicenseToUse',on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    on = 1
    off= 2
    type_status_opendoor=(
        (on,'باز شود.'),
        (off,'باز نشود.')
    )
    status_opendoor=models.IntegerField(choices=type_status_opendoor,default=1,verbose_name='وضعیت باز شدن درب')


class LicenseToUse(models.Model):
    class Meta:
        verbose_name = 'مدیریت lincense بازکردن درب'
        verbose_name_plural = 'مدیریت lincense بازکردن درب'
    rassperypiInfo = models.OneToOneField(RassperySystem, on_delete=models.CASCADE)
    start_lincense=models.DateField(auto_now_add=True)
    end_lincense=models.DateField()

class history(models.Model):
    class Meta:
        verbose_name = 'مدیریت تاریخچه درخواست درب بازشدن'
        verbose_name_plural = 'مدیریت تاریخچه درخواست درب بازشدن'
    rassperypiInfo=models.ForeignKey(RassperySystem,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    member=models.ForeignKey('Members',blank=True,null=True,on_delete=models.CASCADE)
    openDoor=1
    not_allow_openDoor=2
    no_memeber=3
    type_status_request=(
        (openDoor,'در برای فرد باز شد'),
        (not_allow_openDoor,'اجازه برای بازکردن در برای فرد وجود ندارد'),
        (no_memeber,'همچین شخصی تعریف نشده است')
    )
    request_status = models.IntegerField(choices=type_status_request, default=1, verbose_name='وضعیت درخواست')
    picture = models.TextField(verbose_name='عکس شخص')

class Members(models.Model):
    class Meta:
        verbose_name = 'مدیریت افراد برای باز شدن درب'
        verbose_name_plural = 'مدیریت افراد برای باز شدن درب'
    rassperySystem=models.ForeignKey(RassperySystem, on_delete=models.CASCADE)
    add_date=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    change_status_date=models.DateTimeField(auto_now=True)
    allow_openDoor=1
    unallow_openDoor=2
    type_status_members=(
        (allow_openDoor,'فرد اجازه ورود دارد'),
        (unallow_openDoor,'فرد اجازه ورود ندارد')
    )
    allow_status = models.IntegerField(choices=type_status_members, default=1, verbose_name='وضعیت دسترسی فرد')
    picture=models.TextField(verbose_name='عکس شخص')
