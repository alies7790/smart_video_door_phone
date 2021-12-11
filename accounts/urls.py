from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from django.views.decorators.csrf import csrf_exempt
from . import api

app_name='accounts'
urlpatterns=[
 path('login-step1/', api.loginStep1Api.as_view(), name='ورودکاربر مرحله اول'),
 path('login-step2/',csrf_exempt(api.loginStep2Api.as_view()),name='ورود کاربر مرحله دو'),
 path('logout/', csrf_exempt(api.LogoutApi.as_view()), name='خروج کاربر'),
 path('request-send-reset-pass/', api.SendMassegeToResetPasswordAndGetTokenApi.as_view(), name='ارسال پیام احرازهویت ریست پسوورد و دادن توکن'),
 path('recive-codesms-and-send-token/', api.ReciveCodeSmsTokenAndSendTokenApi.as_view(), name='دریافت SMS توکن و ارسال توکن'),
 path('change-password-with-token/', api.ChangePasswordWithTokenApi.as_view(), name='دریافت توکن و تغییر رمز'),
 path('corf/',api.get_csrf_token,name='برای ورود'),

]