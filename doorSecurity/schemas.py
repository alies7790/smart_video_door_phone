import coreapi
from rest_framework.schemas import AutoSchema


class addMember(AutoSchema):
    def get_description(self, path, method):
        return 'add member for door security'
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
                coreapi.Field('hash_serial_rasperyPi'),
                coreapi.Field('title'),
                coreapi.Field('name'),
            #     coreapi.Field('picture'),
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds



class updateMember(AutoSchema):
    def get_description(self, path, method):
        return 'update member: title, name , allow(1 allow, 2 unallow)'
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'patch':
            extra_filds = [
                coreapi.Field('hash_serial_rasperyPi'),
                coreapi.Field('title'),
                coreapi.Field('name'),
                coreapi.Field('id_member'),
                coreapi.Field('allow')
            #     coreapi.Field('picture'),
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds


class getAllMemberDoorSecurity(AutoSchema):
    def get_description(self, path, method):
        return 'get all member doorSecurity,allow_status 1 allow, 2 unallow'
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
                coreapi.Field('hash_serial_rasperyPi'),
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds


class getHistory(AutoSchema):
    def get_description(self, path, method):
        return 'get history doorSecurity,request_status 1 opendoor,2 not_allow_openDoor,3 no_memeber'
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
                coreapi.Field('hash_serial_rasperyPi'),
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds


class changeStatusOpenDoor(AutoSchema):
    def get_description(self, path, method):
        return 'change status openDoor(1 on , 2 off)'
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'patch':
            extra_filds = [
                coreapi.Field('hash_serial_rasperyPi'),
                coreapi.Field('status_openDoor'),
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds

class addHistory(AutoSchema):
    def get_description(self, path, method):
        return 'add history openDoor use in rass not frontEnd, with hash_serial_rasperyPi , token , id_member(not member -1) ,request_status '
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
                coreapi.Field('hash_serial_rasperyPi'),
                coreapi.Field('token'),
                coreapi.Field('id_member'),
                coreapi.Field('request_status'),
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds



class openDoor(AutoSchema):
    def get_description(self, path, method):
        return 'request open door with app'
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'post':
            extra_filds = [
                coreapi.Field('hash_serial_rasperyPi'),
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds