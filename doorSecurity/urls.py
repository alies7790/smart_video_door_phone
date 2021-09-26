from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from . import api

app_name = 'doorSecurity'
urlpatterns = [
    path('open-door/', api.openDoor.as_view(), name='بازکردن درب'),
    path('add-member/', api.addMember.as_view(), name='اضافه کردن اعضا'),
    path('update-member/', api.updateMembers.as_view(), name='تغییر اطلاعات فرد'),
    path('get-all-member/', api.getAllMemberDoorSecurity.as_view(), name='تمام اعضا'),
    path('get-history/', api.getHistory.as_view(), name='تاریخچه'),
]