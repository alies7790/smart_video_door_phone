
import random
from datetime import datetime, timedelta

import jwt
from django.contrib.auth import authenticate, login, logout

import requests
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Profiles, AuthSMS
from rest_framework import  status
from . import schemas,serializers








class loginViews(APIView):
    schema = schemas.loginSchema()
    def post(self, request, *args, **kwargs):
        serializer = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            mobile = data.get('mobile')
            password = data.get('password')
            try:
                profile = Profiles.objects.get(mobile=mobile)

            except:
                return Response({"message": "Username or Password is incorrect."}, status=status.HTTP_401_UNAUTHORIZED)
            user = authenticate(request, username=profile.user.username, password=password)
            if user is not None:
                login(request, user)
                return Response({"message": "You are logged in successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Username or Password is incorrect."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)






class LogoutApi(APIView):
    schema = schemas.logoutSchema()
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return Response({"message": "you are logout."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "not login for logout"}, status=status.HTTP_401_UNAUTHORIZED)











class SendMassegeToResetPasswordApi(APIView):
    schema = schemas.SendMassegeToResetPasswordSchema()
    def post(self, request, *args, **kwargs):
        serializer = serializers.SendMassegeToResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            mobile =data.get('mobile')
            try:
                profile = Profiles.objects.get(mobile=mobile)
            except:
                return Response({"message": "not user with mobile"}, status=status.HTTP_404_NOT_FOUND)
            numberSend = random.randint(100000, 999999)
            url = 'https://RestfulSms.com/api/Token'
            headers = {'Content-Type': 'application/json'}
            body = {'UserApiKey': 'e5788345d42ddd24882a8e7', 'SecretKey': '415##Dlcs&58dsaw34ew'}
            response = requests.post(url, headers=headers, json=body)

            url = 'https://restfulsms.com/api/MessageSend'
            headers = {'Content-Type': 'application/json', 'x-sms-ir-secure-token': response.json()['TokenKey']}
            body = {"Messages": ["کد ارسالی احرازهویت:" + str(numberSend)], "MobileNumbers": [mobile],
                    "LineNumber": "30004603370615", "SendDateTime": "", "CanContinueInCaseOfError": "false"}
            response1 = requests.post(url, headers=headers, json=body)
            for authSms in AuthSMS.objects.filter(profileUser=profile, state_SMS=1):
                authSms.state_SMS = 2
                authSms.save()
            authSMS = AuthSMS.objects.create(profileUser=profile, codeSended=numberSend, type_SMS=1, state_SMS=1)
            return Response({"message": "send SMS for auth rest password"}, status=status.HTTP_200_OK)
        return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)













class ReciveCodeSmsAndSendTokenApi(APIView):
    schema = schemas.ReciveCodeSmsAndSendTokenSchema()
    def post(self,request,*args, **kwargs):
        serializer = serializers.ReciveCodeSmsAndSendTokenSerializer(data=request.data)
        if serializer.is_valid():
            data =serializer.validated_data
            mobile = data.get('mobile')
            sms_code= data.get('sms_code')
            try:
                profile = Profiles.objects.get(mobile=mobile)
            except:
                return Response({"message": "Duplicate code (or other messages)"}, status=status.HTTP_400_BAD_REQUEST)
            try:
                authSMS = AuthSMS.objects.get(profileUser__mobile=mobile, state_SMS=1, codeSended=sms_code)
            except:
                return Response({"message": "sms not send or expire"}, status=status.HTTP_408_REQUEST_TIMEOUT)
            datetimeAuthSms = authSMS.timeSend + timedelta(minutes=2)
            for authSms in AuthSMS.objects.filter(profileUser=profile, state_SMS=3):
                authSms.state_SMS = 2
                authSms.save()
            if datetimeAuthSms > authSMS.timeSend:
                try:
                    dt = datetime.now() + timedelta(minutes=5)
                    encoded_token = jwt.encode(
                        {'user_id': profile.user.username, 'password': profile.user.password},
                        str(sms_code),
                        algorithm='HS256')
                    print(encoded_token)
                    authSMS.token = encoded_token
                    authSMS.state_SMS = 3
                    authSMS.save()
                    return Response({"message": "ok", "token": encoded_token}, status=status.HTTP_200_OK)
                except:
                    return JsonResponse({"message": "Duplicate code (or other messages)"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"message": "expire SMS code"}, status=400)
        else:
            return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)









class ChangePasswordWithTokenApi(APIView):
    schema = schemas.ChangePasswordWithTokenSchema()
    def post(self,request,*args,**kwargs):
        serializer = serializers.ChangePasswordWithTokenSerializer(data=request.data)
        if serializer.is_valid():

            data=serializer.validated_data
            token=data.get('token')
            mobile=data.get('mobile')
            new_password=data.get('new_password')
            repeat_newpassword=data.get('repeat_newpassword')
            try:
                authSMS = AuthSMS.objects.get(profileUser__mobile=mobile, state_SMS=3)
            except:
                return Response({"message": "sms not send or expire"}, status=status.HTTP_408_REQUEST_TIMEOUT)
            try:
                decode_token = jwt.decode(token, str(authSMS.codeSended), algorithms=["HS256"])
                authSMS.state_SMS = 4
                authSMS.save()
            except:
                return Response({"message": "expire token and token not true"}, status=status.HTTP_401_UNAUTHORIZED)

            try:
                profile = Profiles.objects.get(mobile=mobile)
                if new_password == repeat_newpassword:
                    profile.user.set_password(new_password)
                    profile.user.save()
                    profile.save()
                else:
                    return Response({"message": "newPassword and repeatNewPassword not one "}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"message": "not user with information"}, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse({"message": "change pass"}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"message": "Duplicate code (or other messages)"}, status=status.HTTP_400_BAD_REQUEST)
