import coreapi
from rest_framework.schemas import AutoSchema


class addMember(AutoSchema):
    def get_description(self, path, method):
        return 'add member for door security'
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
                coreapi.Field('serial_rasperyPi'),
                coreapi.Field('title'),
            #     coreapi.Field('picture'),
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds



class changeTitleMember(AutoSchema):
    def get_description(self, path, method):
        return 'change title member'
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
                coreapi.Field('serial_rasperyPi'),
                coreapi.Field('title'),
                coreapi.Field('id_member')
            #     coreapi.Field('picture'),
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds


class getAllMemberDoorSecurity(AutoSchema):
    def get_description(self, path, method):
        return 'get all member doorSecurity'
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
                coreapi.Field('serial_rasperyPi'),
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds


class getHistory(AutoSchema):
    def get_description(self, path, method):
        return 'get history doorSecurity'
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
                coreapi.Field('serial_rasperyPi'),
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds


class ChangeMembersAccessPermissions(AutoSchema):
    def get_description(self, path, method):
        return 'Change members access permissions with id member and type allow(1 allow , unallow)'
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
                coreapi.Field('serial_rasperyPi'),
                coreapi.Field('id_member'),
                coreapi.Field('allow'),
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds





class openDoor(AutoSchema):
    def get_description(self, path, method):
        return 'add member to a doorSecurity'
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds