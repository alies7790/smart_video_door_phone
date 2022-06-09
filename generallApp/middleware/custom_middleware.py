# import json
#
# from django.http import JsonResponse
# from django.utils.deprecation import MiddlewareMixin
# from rest_framework import status
# from datetime import date
#
# from rest_framework.authentication import TokenAuthentication
#
# class checkLogin(MiddlewareMixin):
#     WHITELISTED_URLS = [
#         # '/door-security/open-door/',
#         # '/door-security/get-all-member/',
#         # '/door-security/get-history/'
#         # '/door-security/update-member/',
#         # '/door-security/add-member/',
#         # '/accounts/logout/'
#     ]
#     authentication_classes = (TokenAuthentication,)
#     def process_request(self, request):
#         if request.path in self.WHITELISTED_URLS:
#             if request.user.is_authenticated:
#                 return  None
#             else:
#                 return JsonResponse({"message": "no login"},
#                                     status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return None