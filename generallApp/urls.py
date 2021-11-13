from django.urls import path

from . import api

app_name='generalApp'
urlpatterns=[
    path('get-information/',api.getInformations.as_view(),name='اطلاعات سرویس ها')
]