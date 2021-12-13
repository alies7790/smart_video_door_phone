
from django.contrib import admin

# Register your models here.
from accounts.models import Profiles, AuthSMS

from django.contrib import admin

# Register your models here.

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

admin.site.register(Profiles)
admin.site.register(AuthSMS)