
import json

from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.serializers import serialize
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework import  status

from rassperypiInfo.models import RassperySystem
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
                name = data.get('name')
                try:
                    licenseToUse=LicenseToUse.objects.get(rassperypiInfo__profile=Profiles.objects.get(user=request.user),
                                                              rassperypiInfo__serial_rasperyPi=serial_rasperyPi)
                except:
                    return Response({"message": "no lincense for you"},status=status.HTTP_400_BAD_REQUEST)
                try:
                    member = Members.objects.create(title=title, name=name,rassperySystem=licenseToUse.rassperypiInfo)
                    member.save()
                    return Response({"message": "add member succ"}, status=status.HTTP_201_CREATED)
                except:
                    return Response({"message": "please try again later"}, status=status.HTTP_408_REQUEST_TIMEOUT)
            else:
                return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                                status=status.HTTP_400_BAD_REQUEST)





class updateMembers(APIView):
    schema = schemas.updateMember()

    def patch(self, request, *args, **kwargs):
        serializer = serializers.updateMember(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                data = serializer.validated_data
                serial_rasperyPi = data.get('serial_rasperyPi')
                id_member = data.get('id_member')
                allow = data.get('allow')
                name=data.get('name')
                title=data.get('title')
                try:
                    licenseToUse = LicenseToUse.objects.get(
                        rassperypiInfo__profile=Profiles.objects.get(user=request.user),
                        rassperypiInfo__serial_rasperyPi=serial_rasperyPi)
                except:
                    return Response({"message": "no lincense for you"}, status=status.HTTP_400_BAD_REQUEST)
                try:
                    member = Members.objects.get(id=id_member, rassperySystem=licenseToUse.rassperypiInfo)
                    member.allow_status = allow
                    member.title=title
                    member.name=name
                    member.save()
                    return Response({"message": "update member succ"}, status=status.HTTP_201_CREATED)
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
        serializer = serializers.getAllMember(data=request.data)
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
                lis = []
                for member in members:
                    d = {}
                    d['id']=member.id
                    d['title'] = member.title
                    d['name'] = member.name
                    d['add_date'] = member.add_date
                    d['change_status_date'] = member.change_status_date
                    d['allow_status'] = member.allow_status
                    lis.append(d)
                return Response({'members':lis},status=status.HTTP_200_OK)
            else:
                return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)




class getHistory(APIView):
    schema = schemas.getAllMemberDoorSecurity()
    def post(self,request, *args, **kwargs):
        serializer = serializers.getHistory(data=request.data)
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
                lis=[]
                for history in historys:
                    d={}
                    d['id']=history.id
                    if history.member :
                        d['title']=history.member.title
                    d['dateTime']=history.date
                    d['request_status']=history.request_status
                    lis.append(d)
                return Response({'historys':lis}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)






class openDoor(APIView):
    schema = schemas.openDoor()
    def post(self, request, *args, **kwargs):
        serializer = serializers.openDoor(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                data = serializer.validated_data
                serial_rasperyPi = data.get('serial_rasperyPi')
                rassperyInfo=RassperySystem.objects.get(serial_rasperyPi=serial_rasperyPi)
                if rassperyInfo.online_status==1 :
                    channel_layer=get_channel_layer()
                    group_name=f"doorSecurity_{rassperyInfo.serial_rasperyPi}"
                    async_to_sync(channel_layer.group_send)(
                        group_name,
                        {
                            'type':'open_door',
                            'message': json.dumps({'order':'open_door'})
                        })
                    return Response({"message": "open dooring"}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "not online rassperyPi"}, status=status.HTTP_303_SEE_OTHER)
            else:
                return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)