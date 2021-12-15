from rest_framework import serializers



class LoginStep1Serializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11,min_length=11)
    password = serializers.RegexField(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')


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
    new_password=serializers.RegexField(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
    repeat_newpassword=serializers.RegexField(regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

