import json

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status
from datetime import date



from doorSecurity.models import LicenseToUse, InformationService


class exitLincenceMiddleware(MiddlewareMixin):

    WHITELISTED_URLS = [
        '/door-security/open-door/',
        '/door-security/get-all-member/',
        '/door-security/get-history/'
        '/door-security/update-member/',
        '/door-security/add-member/',
        '/door-security/add-history/',
    ]
    def process_request(self, request):
        if request.path in self.WHITELISTED_URLS:
            try:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                serial_rasperyPi = body['serial_rasperyPi']
                licenseToUse=InformationService.objects.get(rassperypiInfo__serial_rasperyPi=str(serial_rasperyPi)).lincense
            except:
                return JsonResponse({"message": "no lincense for you"},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return None


class checkMemberIsForRasspery(MiddlewareMixin):
    WHITELISTED_URLS = [
        '/door-security/open-door/',
        '/door-security/update-member/',
        '/door-security/add-history/',
    ]



class checkLincenseMiddleware(MiddlewareMixin):

    WHITELISTED_URLS = [
        '/door-security/open-door/',
        '/door-security/update-member/',
        '/door-security/add-member/',
    ]

    def process_request(self, request):
        if request.path in self.WHITELISTED_URLS:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            serial_rasperyPi = body['serial_rasperyPi']
            licenseToUse=InformationService.objects.get(rassperypiInfo__serial_rasperyPi=str(serial_rasperyPi)).lincense
            now=date.today()
            if licenseToUse.end_lincense >= now:
                return None
            else:
                return JsonResponse({"message": "end lincence"},
                            status=status.HTTP_404_NOT_FOUND)

        else:
            return None
