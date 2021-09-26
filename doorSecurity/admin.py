from django.contrib import admin

# Register your models here.

from doorSecurity.models import LicenseToUse, HistoryDoorSecurity, Members




admin.site.register(LicenseToUse)
admin.site.register(HistoryDoorSecurity)
admin.site.register(Members)