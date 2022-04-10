from rest_framework import serializers


class addMember(serializers.Serializer):
    hash_serial_rasperyPi = serializers.CharField(max_length=64,min_length=64)
    title = serializers.CharField(max_length=20,min_length=3)
    name = serializers.CharField(max_length=20, min_length=3)
    picture=serializers.CharField()


class openDoor(serializers.Serializer):
    hash_serial_rasperyPi = serializers.CharField(max_length=64,min_length=64)

class getMembersForRassperyPi(serializers.Serializer):
    serial_rasperyPi = serializers.CharField(max_length=16,min_length=16)
    token = serializers.CharField(max_length=5, min_length=5) #test change to 5 to 256
    id_member =serializers.IntegerField(min_value=-1)


class changeStatusOpenDoor(serializers.Serializer):
    hash_serial_rasperyPi = serializers.CharField(max_length=64,min_length=64)
    status_openDoor = serializers.IntegerField(min_value=1, max_value=2)

class addHistory(serializers.Serializer):
    request_status=serializers.IntegerField(min_value=1,max_value=3)
    id_member = serializers.IntegerField()
    token = serializers.CharField(max_length=5, min_length=5) #test change to 5 to 256
    hash_serial_rasperyPi = serializers.CharField(max_length=64,min_length=64)
    picture = serializers.CharField()

class updateMember(serializers.Serializer):
    id_member = serializers.CharField()
    hash_serial_rasperyPi = serializers.CharField(max_length=64, min_length=64,required=False)
    title=serializers.CharField(min_length=3,max_length=20,required=False)
    name = serializers.CharField(min_length=3, max_length=20,required=False)
    allow = serializers.IntegerField(min_value=0, max_value=1,required=False)
    picture = serializers.CharField(required=False)

class getAllMember(serializers.Serializer):
    hash_serial_rasperyPi = serializers.CharField(max_length=64, min_length=64)


class getHistory(serializers.Serializer):
    hash_serial_rasperyPi = serializers.CharField(max_length=64, min_length=64)