from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from . import api

app_name = 'doorSecurity'
urlpatterns = [
    path('open-door/', api.requestOpenDoor.as_view(), name='بازکردن درب'),
    path('add-member/', api.addMember.as_view(), name='اضافه کردن اعضا'),
    path('update-member/', api.updateMember.as_view(), name='تغییر اطلاعات فرد'),
    path('get-all-member-for-front/', api.getAllMember.as_view(), name='گرفتن تمام اعضا'),
    path('get-history/', api.getHistory.as_view(), name='تاریخچه'),
    path('add-history/', api.addHistory.as_view(), name='اضافه کردن ی تارخچه'),
    path('update-status-opendoor/', api.changeStatusOpenDoor.as_view(), name='عوض کردن وضعیت باز کردن درب'),
    path('get-member-for-rass/', api.getMembersForRassperyPi.as_view(), name='گرفتن ممبر برای rass'),
]