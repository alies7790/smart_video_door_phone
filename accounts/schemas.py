import coreapi
from rest_framework.schemas import AutoSchema



class loginSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
                coreapi.Field('mobile'),
                coreapi.Field('password')
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds




class logoutSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'get':
            extra_filds = [
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds




class SendMassegeToResetPasswordSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
                coreapi.Field('mobile'),
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds


class ReciveCodeSmsAndSendTokenSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
                coreapi.Field('mobile'),
                coreapi.Field('sms_code')
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds



class ChangePasswordWithTokenSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds =[
                coreapi.Field('token'),
                coreapi.Field('mobile'),
                coreapi.Field('new_password'),
                coreapi.Field('repeat_newpassword'),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_filds