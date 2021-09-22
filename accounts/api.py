
import random

import requests
from django.contrib.auth import authenticate, login, logout

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Profiles, AuthSMS
from rest_framework import  status

from rassperypiInfo.models import rassperySystem
from . import schemas,serializers,smsHandeller
from . import cryptografyTokenAndSaveToAuthSMS as cryptografy




class loginStep1Api(APIView):
    schema =schemas.loginStep1Schema()
    def post(self, request, *args, **kwargs):
        serializer = serializers.LoginStep1Serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            mobile = data.get('mobile')
            password = data.get('password')

            try:
                profile = Profiles.objects.get(mobile=mobile)
                user = authenticate(request, username=profile.user.username, password=password)
                if user is  None:
                    return Response({"message": "Username or Password is incorrect."},
                                    status=status.HTTP_401_UNAUTHORIZED)

            except:
                return Response({"message": "Username or Password is incorrect."}, status=status.HTTP_401_UNAUTHORIZED)
            # sms_code = random.randint(100000, 999999)
            # status_send_sms = smsHandeller.sendSmS(text_sending="کد ارسالی احرازهویت:", code_sending=sms_code,
            #                                        mobile=[mobile], flag=0)
            sms_code=123456
            status_send_sms=True
            if status_send_sms :
                for authSms in AuthSMS.objects.filter(profileUser=profile, state_SMS=1,type_SMS=2):
                    authSms.state_SMS = 2
                    authSms.save()
                authSMS = AuthSMS.objects.create(profileUser=profile, codeSended=sms_code, type_SMS=2, state_SMS=1)
                encode_information = cryptografy.encodeAndSaveToken(user_id=profile.user.username,
                                                                    password=profile.user.password, authSMS=authSMS,
                                                                    state_SMS=1, time_expire_token=3, sms_code=sms_code)
                if encode_information[0]:
                    return JsonResponse({"message": "ok", "token": encode_information[1]}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"message": "service sms not accesse,please try later time"},
                                        status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({"message": "Duplicate code (or other messages)"},
                                    status=status.HTTP_400_BAD_REQUEST)
        return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)




class loginStep2Api(APIView):
    schema = schemas.loginStep2Schema()

    @csrf_exempt
    def post(self,request,*args,**kwargs):
        serializer = serializers.LoginStep2Serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            token = data.get('token')
            sms_code=data.get('sms_code')
            try:
                auth_sms = AuthSMS.objects.get(state_SMS=1, type_SMS=2, token=token,codeSended=int(sms_code))
                profile = auth_sms.profileUser
                cryptografy.decodeAndSaveStateSMS(authSMS=auth_sms, token=token)
            except:
                return Response({"message": " is incorrect."}, status=status.HTTP_401_UNAUTHORIZED)
            login(request, profile.user)
            return Response({"message": "You are logged in successfully."}, status=status.HTTP_200_OK)
            # if user is not None:
            #
            # else:
            #     return Response({"message": "is incorrect"}, status=status.HTTP_401_UNAUTHORIZED)



        return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)



class LogoutApi(APIView):
    schema = schemas.logoutSchema()

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request.data)
            logout(request)
            return Response({"message": "you are logout."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "not login for logout"}, status=status.HTTP_401_UNAUTHORIZED)











class SendMassegeToResetPasswordAndGetTokenApi(APIView):
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
            # sms_code= random.randint(100000, 999999)
            # status_send_sms=smsHandeller.sendSmS(text_sending="کد ارسالی احرازهویت:",code_sending=sms_code,mobile=[mobile],flag=0)
            sms_code=123456
            status_send_sms=True
            if status_send_sms:
                for authSms in AuthSMS.objects.filter(profileUser=profile, state_SMS=1,type_SMS=1):
                    authSms.state_SMS = 2
                    authSms.save()
                authSMS = AuthSMS.objects.create(profileUser=profile, codeSended=sms_code, type_SMS=1, state_SMS=1)
                encode_information=cryptografy.encodeAndSaveToken(user_id=profile.user.username,password=profile.user.password,authSMS=authSMS,state_SMS=1,time_expire_token=2,sms_code=sms_code)
                if encode_information[0]:
                    return Response({"message": "ok", "token": encode_information[1]}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"message": "Duplicate code (or other messages)"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'success': "Failed,please try again time"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)














class ReciveCodeSmsTokenAndSendTokenApi(APIView):
    schema = schemas.ReciveCodeSmsAndSendTokenSchema()
    def post(self,request,*args, **kwargs):
        serializer = serializers.ReciveCodeSmsAndSendTokenSerializer(data=request.data)
        if serializer.is_valid():
            data =serializer.validated_data
            sms_code= data.get('sms_code')
            token=data.get('token')

            try:
                authSMS = AuthSMS.objects.get(token=token, state_SMS=1, codeSended=sms_code,type_SMS=1)
                try:
                    profile = authSMS.profileUser
                except:
                    return Response({"message": "Duplicate code (or other messages)"},
                                    status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"message": "sms not send or expire"}, status=status.HTTP_408_REQUEST_TIMEOUT)
            for authSms in AuthSMS.objects.filter(profileUser=profile, state_SMS=3,type_SMS=1):
                authSms.state_SMS = 2
                authSms.save()
            cryptografy.decodeAndSaveStateSMS(token=token,authSMS=authSMS)
            if cryptografy.decodeAndSaveStateSMS(token=token,authSMS=authSMS) == False:
                return Response({"message": "expire token and token not true"}, status=status.HTTP_401_UNAUTHORIZED)
            # edit
            encode_information = cryptografy.encodeAndSaveToken(user_id=profile.user.username,
                                                                password=profile.user.password, authSMS=authSMS,
                                                                state_SMS=3, time_expire_token=5,sms_code=authSMS.codeSended)
            if encode_information[0]:

                return Response({"message": "ok", "token": encode_information[1]}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"message": "Duplicate code (or other messages)"}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)









class ChangePasswordWithTokenApi(APIView):
    schema = schemas.ChangePasswordWithTokenSchema()
    def post(self,request,*args,**kwargs):
        serializer = serializers.ChangePasswordWithTokenSerializer(data=request.data)
        if serializer.is_valid():

            data=serializer.validated_data
            token=data.get('token')
            serial_rest_password=data.get('serial_rest_password')
            new_password=data.get('new_password')
            repeat_newpassword=data.get('repeat_newpassword')
            try:
                authSMS = AuthSMS.objects.get(token=token, state_SMS=3,type_SMS=1)
            except:
                return Response({"message": "sms not send or expire"}, status=status.HTTP_401_UNAUTHORIZED)
            if cryptografy.decodeAndSaveStateSMS(token=token,authSMS=authSMS) == False:
                return Response({"message": "expire token and token not true"}, status=status.HTTP_401_UNAUTHORIZED)

            try:
                profile = authSMS.profileUser
                try:
                    rasspery_system = rassperySystem.objects.get(profile=profile,serial_reset_password=serial_rest_password)
                except:
                    return Response({"message": "not ture serial reset"}, status=status.HTTP_401_UNAUTHORIZED)
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
