from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from . import api

app_name='accounts'
urlpatterns=[
 path('login/', api.loginViews.as_view(), name='ورودکاربر'),
 path('logout/', api.LogoutApi.as_view(), name='خروج کاربر'),
 path('requestSendResetPass/', api.SendMassegeToResetPasswordApi.as_view(), name='ارسال پیام احرازهویت ریست پسوورد'),
 path('reciveCodeSmsAndSendTokrn/', api.ReciveCodeSmsAndSendTokenApi.as_view(), name='دریافت SMS و ارسال توکن'),
 path('changePasswordWithToken/', api.ChangePasswordWithTokenApi.as_view(), name='دریافت توکن و تغییر رمز')

]