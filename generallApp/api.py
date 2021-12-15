from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import Profiles
from doorSecurity.models import InformationService as InformationDoorSecurity
from generallApp import schemas, serializers


class getInformations(APIView):
    schema = schemas.getInformationSchema()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def get(self,request, *args, **kwargs):
        serializer = serializers.getInformatonSerializer(data=request.data)
        if serializer.is_valid():
            info={}
            try:
                informationDoorSecuritys = InformationDoorSecurity.objects.filter(
                    rassperypiInfo__profile=Profiles.objects.get(user=request.user), )
                info['doorSecurity']=[]
                for infoSec in informationDoorSecuritys:

                    info['doorSecurity'].append({'title':infoSec.title,
                                                 'address':infoSec.rassperypiInfo.address,
                                                 'hash_serial_rasperyPi':infoSec.rassperypiInfo.hash_serial_rassperyPi})
            except:
                return Response({"message": "please try later"}, status=status.HTTP_408_REQUEST_TIMEOUT)

            return Response(info, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Duplicate code (or other messages)"},
                            status=status.HTTP_400_BAD_REQUEST)
