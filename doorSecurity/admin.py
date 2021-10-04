from django.contrib import admin

# Register your models here.

from doorSecurity.models import LicenseToUse, history, Members




admin.site.register(LicenseToUse)
admin.site.register(history)
admin.site.register(Members)