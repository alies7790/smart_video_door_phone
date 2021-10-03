from rest_framework import serializers


class addMember(serializers.Serializer):
    serial_rasperyPi = serializers.CharField(max_length=16,min_length=16)
    title = serializers.CharField(max_length=20,min_length=3)
    name = serializers.CharField(max_length=20, min_length=3)
#     picture


class openDoor(serializers.Serializer):
    serial_rasperyPi = serializers.CharField(max_length=16,min_length=16)

class updateMember(serializers.Serializer):
    id_member = serializers.CharField()
    serial_rasperyPi = serializers.CharField(max_length=16, min_length=16)
    title=serializers.CharField(min_length=3,max_length=20)
    name = serializers.CharField(min_length=3, max_length=20)
    allow = serializers.IntegerField(min_value=1, max_value=2)

class getAllMember(serializers.Serializer):
    serial_rasperyPi = serializers.CharField(max_length=16, min_length=16)


class getHistory(serializers.Serializer):
    serial_rasperyPi = serializers.CharField(max_length=16, min_length=16)