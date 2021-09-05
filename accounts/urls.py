from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from . import api

app_name='accounts'
urlpatterns=[
 path('loginStep1/', api.loginStep1Api.as_view(), name='ورودکاربر مرحله اول'),
 path('loginStep2/',api.loginStep2Api.as_view(),name='ورود کاربر مرحله دو'),
 path('logout/', api.LogoutApi.as_view(), name='خروج کاربر'),
 path('requestSendResetPass/', api.SendMassegeToResetPasswordAndGetTokenApi.as_view(), name='ارسال پیام احرازهویت ریست پسوورد و دادن توکن'),
 path('reciveCodeSmsAndSendToken/', api.ReciveCodeSmsTokenAndSendTokenApi.as_view(), name='دریافت SMS توکن و ارسال توکن'),
 path('changePasswordWithToken/', api.ChangePasswordWithTokenApi.as_view(), name='دریافت توکن و تغییر رمز')

]