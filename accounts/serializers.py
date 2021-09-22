from rest_framework import serializers



class LoginStep1Serializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11,min_length=11)
    password = serializers.CharField()


class LoginStep2Serializer(serializers.Serializer):
    token = serializers.CharField()
    sms_code=serializers.CharField(max_length=6,min_length=6)



class SendMassegeToResetPasswordSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11,min_length=11)


class ReciveCodeSmsAndSendTokenSerializer(serializers.Serializer):
    sms_code=serializers.CharField(max_length=6,min_length=6)
    token = serializers.CharField()

class ChangePasswordWithTokenSerializer(serializers.Serializer):
    serial_rest_password=serializers.CharField(max_length=12,min_length=12)
    token = serializers.CharField()
    new_password=serializers.CharField()
    repeat_newpassword=serializers.CharField()
