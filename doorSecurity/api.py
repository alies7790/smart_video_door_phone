
import json

from rest_framework.response import Response
from rest_framework.views import APIView
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework import  status

from rassperypiInfo.models import RassperySystem
from . import schemas,serializers
from accounts.models import Profiles
from .models import  Members, history, InformationService


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
                    informationService=InformationService.objects.get(rassperypiInfo__profile=Profiles.objects.get(user=request.user),
                                                              rassperypiInfo__serial_rasperyPi=serial_rasperyPi,)
                except:
                    return Response({"message": "no lincense for you"},status=status.HTTP_400_BAD_REQUEST)
                try:
                    member = Members.objects.create(title=title, name=name,rassperySystem=informationService.rassperypiInfo)
                    member.save()
                    return Response({"message": "add member succ"}, status=status.HTTP_201_CREATED)
                except:
                    return Response({"message": "please try again later"}, status=status.HTTP_408_REQUEST_TIMEOUT)
            else:
                return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                                status=status.HTTP_400_BAD_REQUEST)





class updateMember(APIView):
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
                informationService = InformationService.objects.get(rassperypiInfo__profile=Profiles.objects.get(user=request.user),
                                                              rassperypiInfo__serial_rasperyPi=serial_rasperyPi,)
                try:
                    member = Members.objects.get(id=id_member, rassperySystem=informationService.rassperypiInfo)
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
                historys=history.objects.filter(rassperypiInfo__serial_rasperyPi=serial_rasperyPi).order_by('date')
                lis=[]
                for i in historys:
                    d={}
                    d['id']=i.id
                    if i.member :
                        d['title']=i.member.title
                    d['dateTime']=i.date
                    d['request_status']=i.request_status
                    lis.append(d)
                return Response({'historys':lis}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)


class changeStatusOpenDoor(APIView):
    schema = schemas.changeStatusOpenDoor()
    def patch(self , request, *args, **kwargs):
        serializer=serializers.changeStatusOpenDoor(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            serial_rasperyPi = data.get('serial_rasperyPi')
            status_openDoor = data.get('status_openDoor')
            try:
                informationService = InformationService.objects.get(rassperypiInfo__serial_rasperyPi=serial_rasperyPi)
                informationService.status_opendoor=status_openDoor
                informationService.save()
                channel_layer = get_channel_layer()
                group_name = f"doorSecurity_{informationService.rassperypiInfo.serial_rasperyPi}"
                async_to_sync(channel_layer.group_send)(
                    group_name,
                    {
                        'type': 'sendMassege',
                        'message': json.dumps({'massege': 'change status openDoor', 'code': (1011+status_openDoor)})
                    })
                return  Response({"message":"ok"},status=status.HTTP_200_OK)
            except:
                return Response({"message": "please try again,later"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)


class addHistory(APIView):
    schema = schemas.addHistory()
    def post(self, request, *args, **kwargs):
        serializer = serializers.addHistory(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            serial_rasperyPi = data.get('serial_rasperyPi')
            token = data.get('token')
            request_status=data.get('request_status')
            id_member=data.get('id_member')
            try:
                rassperyInfo=RassperySystem.objects.get(serial_rasperyPi=serial_rasperyPi,token=token)
            except:
                return Response({"message": "rassperyPi does not exist with these specifications"},
                                status=status.HTTP_400_BAD_REQUEST)
            try:
                if id_member==-1:
                    history_created=history.objects.create(rassperypiInfo=rassperyInfo,request_status=3)
                else:
                    history_created = history.objects.create(rassperypiInfo=rassperyInfo, request_status=request_status,member_id=id_member)
            except:
                return Response({"message": "information not true or server busy,please check information send again"},
                                status=status.HTTP_400_BAD_REQUEST)
            history_created.save()
            return Response({"message": "add history succ"}, status=status.HTTP_201_CREATED)

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
                try:
                    rassperyInfo=RassperySystem.objects.get(serial_rasperyPi=serial_rasperyPi,profile__user=request.user)
                except:
                    return Response({"message": "rassperyPi does not exist with these specifications"},
                                    status=status.HTTP_400_BAD_REQUEST)
                if rassperyInfo.online_status==1 :
                    channel_layer=get_channel_layer()
                    group_name=f"doorSecurity_{rassperyInfo.serial_rasperyPi}"
                    async_to_sync(channel_layer.group_send)(
                        group_name,
                        {
                            'type':'sendMassege',
                            'message': json.dumps({'massege':'open Door','code':1011})
                        })
                    return Response({"message": "open dooring"}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "not online rassperyPi"}, status=status.HTTP_303_SEE_OTHER)
            else:
                return Response({"message": "not login"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)