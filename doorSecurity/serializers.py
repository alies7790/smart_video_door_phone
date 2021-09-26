from rest_framework import serializers


class addMember(serializers.Serializer):
    serial_rasperyPi = serializers.CharField(max_length=16,min_length=16)
    title = serializers.CharField(max_length=20,min_length=3)
#     picture


class ChangeMembersAccessPermissions(serializers.Serializer):
    id_member=serializers.CharField()
    serial_rasperyPi = serializers.CharField(max_length=16, min_length=16)
    allow=serializers.IntegerField(min_value=1,max_value=2)


class changeTitleMember(serializers.Serializer):
    id_member=serializers.CharField()
    serial_rasperyPi = serializers.CharField(max_length=16, min_length=16)
    title=serializers.CharField(max_length=20,min_length=3)


class getAllMemberDoorSecurity(serializers.Serializer):
    serial_rasperyPi = serializers.CharField(max_length=16, min_length=16)


class getHistory(serializers.Serializer):
    serial_rasperyPi = serializers.CharField(max_length=16, min_length=16)