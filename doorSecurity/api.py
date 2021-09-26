
import json

from rest_framework.response import Response
from rest_framework.views import APIView

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework import  status
from . import schemas,serializers
from accounts.models import Profiles
from .models import LicenseToUse, Members, HistoryDoorSecurity


class addMember(APIView):
    schema=schemas.addMember()
    def post(self,request, *args, **kwargs):
        serializer = serializers.addMember(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                data = serializer.validated_data
                serial_rasperyPi=data.get('serial_rasperyPi')
                title=data.get('title')
                try:
                    licenseToUse=LicenseToUse.objects.get(rassperypiInfo__profile=Profiles.objects.get(user=request.user),
                                                              rassperypiInfo__serial_rasperyPi=serial_rasperyPi)
                except:
                    return Response({"message": "no lincense for you"},status=status.HTTP_400_BAD_REQUEST)
                try:
                    member = Members.objects.create(title_member=title, rassperySystem=licenseToUse.rassperypiInfo)
                    member.save()
                    return Response({"message": "add member succ"}, status=status.HTTP_201_CREATED)
                except:
                    return Response({"message": "please try again later"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                                status=status.HTTP_400_BAD_REQUEST)




class ChangeMembersAccessPermissions(APIView):
    schema = schemas.ChangeMembersAccessPermissions()
    def post(self,request, *args, **kwargs):
        serializer = serializers.addMember(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                data = serializer.validated_data
                serial_rasperyPi=data.get('serial_rasperyPi')
                id_member=data.get('id_member')
                allow=data.get('allow')
                try:
                    licenseToUse=LicenseToUse.objects.get(rassperypiInfo__profile=Profiles.objects.get(user=request.user),
                                                              rassperypiInfo__serial_rasperyPi=serial_rasperyPi)
                except:
                    return Response({"message": "no lincense for you"}, status=status.HTTP_400_BAD_REQUEST)
                try:
                    member = Members.objects.get(id=id_member,rassperySystem=licenseToUse.rassperypiInfo)
                    member.allow_status=allow
                    member.save()
                    return Response({"message": "add member succ"}, status=status.HTTP_201_CREATED)
                except:
                    return Response({"message": "please try again later"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)





class changeTitleMember(APIView):
    schema = schemas.ChangeMembersAccessPermissions()
    def post(self,request, *args, **kwargs):
        serializer = serializers.changeTitleMember(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                data = serializer.validated_data
                serial_rasperyPi = data.get('serial_rasperyPi')
                id_member = data.get('id_member')
                title = data.get('title')
                try:
                    licenseToUse=LicenseToUse.objects.get(rassperypiInfo__profile=Profiles.objects.get(user=request.user),
                                                              rassperypiInfo__serial_rasperyPi=serial_rasperyPi)
                except:
                    return Response({"message": "no lincense for you"}, status=status.HTTP_400_BAD_REQUEST)
                try:
                    member = Members.objects.get(id=id_member,rassperySystem=licenseToUse.rassperypiInfo)
                    member.title_member=title
                    member.save()
                    return Response({"message": "add member succ"}, status=status.HTTP_201_CREATED)
                except:
                    return Response({"message": "please try again later"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)




class getAllMemberDoorSecurity(APIView):
    schema = schemas.getAllMemberDoorSecurity()
    def post(self,request, *args, **kwargs):
        serializer = serializers.getAllMemberDoorSecurity(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                data = serializer.validated_data
                serial_rasperyPi = data.get('serial_rasperyPi')
                try:
                    licenseToUse=LicenseToUse.objects.get(rassperypiInfo__profile=Profiles.objects.get(user=request.user),
                                                              rassperypiInfo__serial_rasperyPi=serial_rasperyPi)
                except:
                    return Response({"message": "no lincense for you"}, status=status.HTTP_400_BAD_REQUEST)

                members=Members.objects.filter(rassperySystem__serial_rasperyPi=serial_rasperyPi).order_by('add_date')
                return Response({members},status=status.HTTP_200_OK)
            else:
                return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)




class getHistory(APIView):
    schema = schemas.getAllMemberDoorSecurity()
    def post(self,request, *args, **kwargs):
        serializer = serializers.getAllMemberDoorSecurity(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                data = serializer.validated_data
                serial_rasperyPi = data.get('serial_rasperyPi')
                try:
                    licenseToUse=LicenseToUse.objects.get(rassperypiInfo__profile=Profiles.objects.get(user=request.user),
                                                              rassperypiInfo__serial_rasperyPi=serial_rasperyPi)
                except:
                    return Response({"message": "no lincense for you"}, status=status.HTTP_400_BAD_REQUEST)
                historys=HistoryDoorSecurity.objects.filter(rassperypiInfo__serial_rasperyPi=serial_rasperyPi).order_by('date')
                return Response({historys}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)






class openDoor(APIView):
    schema = schemas.openDoor()
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            profile=Profiles.objects.get(user_id=request.user.id)
            channel_layer=get_channel_layer()
            group_name=f"doorSecurity_{profile.rasspery.token}"
            async_to_sync(channel_layer.group_send)(
                group_name,
                {
                    'type':'open_door',
                    'message': json.dumps({'order':'open_door'})
                })
        else:
            return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)



# class addMember(APIView):
#
