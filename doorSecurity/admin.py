from django.contrib import admin

# Register your models here.

from doorSecurity.models import LicenseToUse, history, Members ,InformationService



admin.site.register(InformationService)
admin.site.register(LicenseToUse)
admin.site.register(history)
admin.site.register(Members)