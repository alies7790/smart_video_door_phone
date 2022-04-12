
import json



from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework import  status

from rassperypiInfo.models import RassperySystem
from . import schemas,serializers
from accounts.models import Profiles
from .models import  Members, history, InformationService
from .resize_image import resizeImage


class addMember(APIView):
    schema=schemas.addMember()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def post(self,request, *args, **kwargs):
        serializer = serializers.addMember(data=request.data)
        if serializer.is_valid():
                data = serializer.validated_data
                hash_serial_rasperyPi=data.get('hash_serial_rasperyPi')
                title=data.get('title')
                name = data.get('name')
                picture = data.get('picture')
                picture = resizeImage(picture)
                if picture == False:
                    return Response({"message": "image not base64"},
                             status=status.HTTP_400_BAD_REQUEST)

                try:
                    informationService=InformationService.objects.get(rassperypiInfo__profile=Profiles.objects.get(user=request.user),
                                                              rassperypiInfo__hash_serial_rassperyPi=hash_serial_rasperyPi,)
                except:
                    return Response({"message": "please try later"},status=status.HTTP_408_REQUEST_TIMEOUT)
                try:
                    member = Members.objects.create(title=title,picture=picture, name=name,rassperySystem=informationService.rassperypiInfo)
                    member.save()
                    channel_layer = get_channel_layer()
                    group_name = f"doorSecurity_{informationService.rassperypiInfo.serial_rasperyPi}"
                    async_to_sync(channel_layer.group_send)(
                        group_name,
                        {
                            'type': 'sendMassege',
                            'message': json.dumps({'massege': 'add member new', 'code': 1014 , 'id_member':member.id})
                        })
                    return Response({"message": "add member succ"}, status=status.HTTP_201_CREATED)
                except:
                    return Response({"message": "please try again later"}, status=status.HTTP_408_REQUEST_TIMEOUT)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                                status=status.HTTP_400_BAD_REQUEST)





class updateMember(APIView):
    schema = schemas.updateMember()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def patch(self, request, *args, **kwargs):
        serializer = serializers.updateMember(data=request.data)
        if serializer.is_valid():
                data = serializer.validated_data
                hash_serial_rasperyPi = data.get('hash_serial_rasperyPi')
                id_member = int(data.get('id_member'))
                allow = data.get('allow')
                name=data.get('name')
                title=data.get('title')
                picture=data.get('picture')
                informationService = InformationService.objects.get(rassperypiInfo__profile=Profiles.objects.get(user=request.user),
                                                              rassperypiInfo__hash_serial_rassperyPi=hash_serial_rasperyPi,)
                try:
                    picture = resizeImage(picture)
                    if picture == False:
                        return  Response({"message": "not base64"},
                                 status=status.HTTP_400_BAD_REQUEST)
                    member = Members.objects.get(id=id_member, rassperySystem=informationService.rassperypiInfo)
                    member.allow_status = allow
                    member.title=title
                    member.name=name
                    member.picture = picture

                    member.save()
                    channel_layer = get_channel_layer()
                    group_name = f"doorSecurity_{informationService.rassperypiInfo.serial_rasperyPi}"
                    async_to_sync(channel_layer.group_send)(
                        group_name,
                        {
                            'type': 'sendMassege',
                            'message': json.dumps({'massege': 'update member', 'code': 1015 , 'id_member':member.id})
                        })
                    return Response({"message": "update member succ"}, status=status.HTTP_200_OK)
                except:
                    return Response({"message": "please try again later"}, status=status.HTTP_408_REQUEST_TIMEOUT)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)


class getAllMember(APIView):
    schema = schemas.getAllMemberDoorSecurity()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def post(self,request, *args, **kwargs):
        serializer = serializers.getAllMember(data=request.data)
        if serializer.is_valid():
                data = serializer.validated_data
                hash_serial_rasperyPi = data.get('hash_serial_rasperyPi')
                members=Members.objects.filter(rassperySystem__hash_serial_rassperyPi=hash_serial_rasperyPi).order_by('add_date')
                lis = []
                for member in members:
                    d = {}
                    d['id']=member.id
                    d['title'] = member.title
                    d['name'] = member.name
                    d['add_date'] = member.add_date
                    d['change_status_date'] = member.change_status_date
                    d['allow_status'] = member.allow_status
                    d['picture'] = member.picture
                    lis.append(d)
                return Response({'members':lis},status=status.HTTP_200_OK)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)




class getHistory(APIView):
    schema = schemas.getAllMemberDoorSecurity()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def post(self,request, *args, **kwargs):
        serializer = serializers.getHistory(data=request.data)
        if serializer.is_valid():
                data = serializer.validated_data
                hash_serial_rasperyPi = data.get('hash_serial_rasperyPi')
                historys=history.objects.filter(rassperypiInfo__hash_serial_rassperyPi=hash_serial_rasperyPi).order_by('date')
                lis=[]
                for i in historys:
                    d={}
                    d['id']=i.id
                    if i.member :
                        d['title']=i.member.title
                        d['name'] = i.member.name
                    else:
                        d['title'] = None
                        d['name'] = None
                    d['picture'] = i.member.picture
                    d['dateTime']=i.date
                    d['request_status']=i.request_status
                    lis.append(d)
                return Response({'historys':lis}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)


class changeStatusOpenDoor(APIView):
    schema = schemas.changeStatusOpenDoor()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def patch(self , request, *args, **kwargs):
        serializer=serializers.changeStatusOpenDoor(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            hash_serial_rasperyPi = data.get('hash_serial_rasperyPi')
            status_openDoor = data.get('status_openDoor')
            try:
                informationService = InformationService.objects.get(rassperypiInfo__hash_serial_rassperyPi=hash_serial_rasperyPi)
                informationService.status_opendoor=status_openDoor
                informationService.save()
                channel_layer = get_channel_layer()
                group_name = f"doorSecurity_{informationService.rassperypiInfo.hash_serial_rassperyPi}"
                async_to_sync(channel_layer.group_send)(
                    group_name,
                    {
                        'type': 'sendMassege',
                        'message': json.dumps({'massege': 'change status requestOpenDoor', 'code': (1011+status_openDoor)})
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
            hash_serial_rasperyPi = data.get('hash_serial_rasperyPi')
            token = data.get('token')
            request_status=data.get('request_status')
            id_member=data.get('id_member')
            picture = data.get('picture')
            picture = resizeImage(picture)
            if picture ==False:
                Response({"message": "not base64"},
                         status=status.HTTP_400_BAD_REQUEST)
            try:
                rassperyInfo=RassperySystem.objects.get(hash_serial_rassperyPi=hash_serial_rasperyPi,token_connect_rassperypi=token)
            except:
                return Response({"message": "rassperyPi does not exist with these specifications"},
                                status=status.HTTP_400_BAD_REQUEST)
            # try:
            if id_member==-1:
                history_created=history.objects.create(rassperypiInfo=rassperyInfo,request_status=3,picture=picture)
            else:
                history_created = history.objects.create(rassperypiInfo=rassperyInfo, picture=picture,request_status=request_status,member_id=id_member)
        # except:
            #     return Response({"message": "information not true or server busy,please check information send again"},
            #                     status=status.HTTP_400_BAD_REQUEST)
            history_created.save()
            return Response({"message": "add history succ"}, status=status.HTTP_201_CREATED)

        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)





class requestOpenDoor(APIView):
    schema = schemas.openDoor()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def post(self, request, *args, **kwargs):
        serializer = serializers.openDoor(data=request.data)
        if serializer.is_valid():
                data = serializer.validated_data
                hash_serial_rasperyPi = data.get('hash_serial_rasperyPi')
                try:
                    rassperyInfo=RassperySystem.objects.get(hash_serial_rassperyPi=hash_serial_rasperyPi,profile__user=request.user)
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
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)



class getMembersForRassperyPi(APIView):
    schema = schemas.getMembersForRassSchema()
    def post(self, request, *args, **kwargs):
        global lis
        serializer = serializers.getMembersForRassperyPi(data=request.data)
        if serializer.is_valid():
                data = serializer.validated_data
                serial_rasperyPi = data.get('serial_rasperyPi')
                token = data.get('token')
                id_member = data.get('id_member')
                try:
                    rassperyInfo = RassperySystem.objects.get(serial_rasperyPi=serial_rasperyPi,
                                                              token_connect_rassperypi=token)
                except:
                    return Response({"message": "rassperyPi does not exist with these specifications"},
                                    status=status.HTTP_400_BAD_REQUEST)
                if id_member == -1:
                    members = Members.objects.filter(
                        rassperySystem__serial_rasperyPi=serial_rasperyPi).order_by('add_date')
                    lis = []
                    for member in members:
                        d = {}
                        d['id'] = member.id
                        d['title'] = member.title
                        d['name'] = member.name
                        d['add_date'] = member.add_date
                        d['change_status_date'] = member.change_status_date
                        d['allow_status'] = member.allow_status
                        d['picture'] = member.picture
                        lis.append(d)
                    return Response({'members': lis,'code':1016}, status=status.HTTP_200_OK)
                else:
                    try:
                        member = Members.objects.get(
                            rassperySystem__serial_rasperyPi=serial_rasperyPi, id=id_member)
                        lis = []
                        d = {}
                        d['id'] = member.id
                        d['title'] = member.title
                        d['name'] = member.name
                        d['add_date'] = member.add_date
                        d['change_status_date'] = member.change_status_date
                        d['allow_status'] = member.allow_status
                        d['picture'] = member.picture
                        lis.append(d)
                        return Response({'code': 1016, 'members': lis}, status=status.HTTP_200_OK)
                    except:
                        return Response({'code':1017}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)



class deleteMember():
    pass
