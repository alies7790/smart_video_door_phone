
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profiles(models.Model):
    class Meta:
        verbose_name = 'نمایه کاربری'
        verbose_name_plural = 'نمایه کاربری'

    user=models.OneToOneField(User ,on_delete=models.CASCADE, verbose_name='حساب کاربری')
    mobile=models.CharField('تلفن همراه',max_length=11,unique=True)

    def __str__(self):
        return self.user.get_full_name()

class AuthSMS(models.Model):
    class Meta:
        verbose_name = 'SMSهای احراز هویت'
        verbose_name_plural = 'SMSهای احراز هویت'
    profileUser=models.ForeignKey(Profiles,on_delete=models.CASCADE,verbose_name='پروفایل فرد مورد احراز')
    timeSend=models.DateTimeField('تایم ارسال SMS',auto_now_add=True)
    codeSended=models.IntegerField('کد ارسال شده')
    token = models.CharField('توکن برای احراز',max_length=300)
    resetPass = 1
    authMobile = 2
    types_SMS = (
        (resetPass, 'ریست کردن پسوورد'),
        (authMobile, 'احراز موبایل')
    )
    type_SMS = models.IntegerField(choices=types_SMS, verbose_name='نوع پیام')
    sendSMS=1
    expireSMS=2
    useSMS=3
    changePass=4
    states_SMS = (
        (sendSMS, 'پیام ارسال شده'),
        (expireSMS,'منقضی شده'),
        (useSMS,'از پیام برای احراز استفاده شده'),
        (changePass, 'از پیام برای تغییر رمز استفاده شد')
    )
    state_SMS = models.IntegerField(choices=states_SMS, default=1, verbose_name='وضعیت پیام')
    def __str__(self):
        return self.profileUser.user.get_username()