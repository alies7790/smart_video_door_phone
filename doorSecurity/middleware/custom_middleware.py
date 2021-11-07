import json

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status
from datetime import date



from doorSecurity.models import LicenseToUse, InformationService, Members


class checkLogin(MiddlewareMixin):
    WHITELISTED_URLS = [
        '/door-security/open-door/',
        '/door-security/get-all-member/',
        '/door-security/get-history/'
        '/door-security/update-member/',
        '/door-security/add-member/',
    ]
    def process_request(self, request):
        if request.path in self.WHITELISTED_URLS:
            if request.user.is_authenticated:
                print("kkk")
                return  None
            else:
                return JsonResponse({"message": "no login"},
                                    status=status.HTTP_401_UNAUTHORIZED)
        else:
            return None

class checkHashRassSerial(MiddlewareMixin):
    WHITELISTED_URLS = [
        '/door-security/open-door/',
        '/door-security/get-all-member/',
        '/door-security/get-history/'
        '/door-security/update-member/',
        '/door-security/add-member/',
    ]
    def process_request(self, request):
        if request.path in self.WHITELISTED_URLS:
            try:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                hash_serial_rasperyPi = body['hash_serial_rasperyPi']
                licenseToUse = InformationService.objects.get(
                    rassperypiInfo__hash_serial_rasperyPi=str(hash_serial_rasperyPi),rassperypiInfo__profile__user=request.user).lincense
            except:
                return JsonResponse({"message": "Duplicate code (or other messages)"},
                                status=status.HTTP_400_BAD_REQUEST)

            try:
                licenseToUse = InformationService.objects.get(
                    rassperypiInfo__hash_serial_rasperyPi=str(hash_serial_rasperyPi),
                    rassperypiInfo__profile__user=request.user).lincense
            except:
                return JsonResponse({"message": "no hash rassperyPi for you"},
                                    status=status.HTTP_404_NOT_FOUND)
            return None
        else:
            return None
class exitLincenceMiddleware(MiddlewareMixin):

    WHITELISTED_URLS = [
        '/door-security/open-door/',
        '/door-security/get-all-member/',
        '/door-security/get-history/'
        '/door-security/update-member/',
        '/door-security/add-member/',
    ]
    def process_request(self, request):
        if request.path in self.WHITELISTED_URLS:
            try:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                serial_rasperyPi = body['hash_serial_rasperyPi']
            except:
                return JsonResponse({"message": "Duplicate code (or other messages)"},
                                status=status.HTTP_400_BAD_REQUEST)

            try:
                licenseToUse=InformationService.objects.get(rassperypiInfo__serial_rasperyPi=str(serial_rasperyPi)).lincense
            except:
                return JsonResponse({"message": "no lincense for you"},
                                status=status.HTTP_404_NOT_FOUND)
            return None
        else:
            return None


class checkMemberIsForRasspery(MiddlewareMixin):
    WHITELISTED_URLS = [
        '/door-security/update-member/',
        '/door-security/add-history/',
    ]
    def process_request(self, request):
        if request.path in self.WHITELISTED_URLS:
            try:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                serial_rasperyPi = body['hash_serial_rasperyPi']
                id_member = body['id_member']
            except:
                return JsonResponse({"message": "Duplicate code (or other messages)"},
                                status=status.HTTP_400_BAD_REQUEST)

            try:
                member = Members.objects.get(id=id_member, rassperySystem__serial_rasperyPi=serial_rasperyPi)
            except:
                return JsonResponse({"message": "no member exit for you"},
                                    status=status.HTTP_404_NOT_FOUND)
            return None
        else:
            return None


class checkLincenseMiddleware(MiddlewareMixin):

    WHITELISTED_URLS = [
        '/door-security/open-door/',
        '/door-security/update-member/',
        '/door-security/add-member/',
    ]

    def process_request(self, request):
        if request.path in self.WHITELISTED_URLS:
            try:
                body_unicode = request.body.decode('utf-8')
                body = json.loads(body_unicode)
                serial_rasperyPi = body['hash_serial_rasperyPi']
                licenseToUse = InformationService.objects.get(
                    rassperypiInfo__serial_rasperyPi=str(serial_rasperyPi)).lincense
                now = date.today()
            except:
                return JsonResponse({"message": "Duplicate code (or other messages)"},
                                status=status.HTTP_400_BAD_REQUEST)

            if licenseToUse.end_lincense >= now:
                return None
            else:
                return JsonResponse({"message": "end lincence"},
                            status=status.HTTP_404_NOT_FOUND)

        else:
            return None
