from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from . import api

app_name = 'doorSecurity'
urlpatterns = [
    path('open_door/', api.openDoor.as_view(), name='بازکردن درب'),
    path('add_member/', api.addMember.as_view(), name='اضافه کردن اعضا'),
    path('Change_member_allow/', api.ChangeMembersAccessPermissions.as_view(), name='تغییر دسترسی فرد'),
    path('chang_title_member/', api.changeTitleMember.as_view(), name='تغییر عنوان فرد'),
    path('get_allMember_doorSecurity/', api.getAllMemberDoorSecurity.as_view(), name='تمام اعضا'),
    path('get_history/', api.getHistory.as_view(), name='تاریخچه'),
]