import coreapi
from rest_framework.schemas import AutoSchema


class getInformationSchema(AutoSchema):
    def get_description(self, path, method):
        return 'for login Step1'
    def get_manual_fields(self, path, method):
        extra_filds=[]
        if method.lower() == 'get':
            extra_filds = [
            ]
        manual_fields= super().get_manual_fields(path,method)
        return  manual_fields + extra_filds