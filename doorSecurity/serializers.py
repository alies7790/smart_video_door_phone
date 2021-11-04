from rest_framework import serializers


class addMember(serializers.Serializer):
    hash_serial_rasperyPi = serializers.CharField(max_length=16,min_length=16)
    title = serializers.CharField(max_length=20,min_length=3)
    name = serializers.CharField(max_length=20, min_length=3)
#     picture


class openDoor(serializers.Serializer):
    hash_serial_rasperyPi = serializers.CharField(max_length=16,min_length=16)


class changeStatusOpenDoor(serializers.Serializer):
    hash_serial_rasperyPi = serializers.CharField(max_length=16,min_length=16)
    status_openDoor = serializers.IntegerField(min_value=1, max_value=2)

class addHistory(serializers.Serializer):
    request_status=serializers.IntegerField(min_value=1,max_value=3)
    id_member = serializers.IntegerField()
    token = serializers.CharField(max_length=5, min_length=5) #test change to 5 to 256
    hash_serial_rasperyPi = serializers.CharField(max_length=16,min_length=16)

class updateMember(serializers.Serializer):
    id_member = serializers.CharField()
    hash_serial_rasperyPi = serializers.CharField(max_length=16, min_length=16)
    title=serializers.CharField(min_length=3,max_length=20)
    name = serializers.CharField(min_length=3, max_length=20)
    allow = serializers.IntegerField(min_value=1, max_value=2)

class getAllMember(serializers.Serializer):
    hash_serial_rasperyPi = serializers.CharField(max_length=16, min_length=16)


class getHistory(serializers.Serializer):
    hash_serial_rasperyPi = serializers.CharField(max_length=16, min_length=16)