
from datetime import datetime, timedelta
import jwt


def encodeAndSaveToken(user_id,password,sms_code,authSMS,state_SMS,time_expire_token):
    try:
        dt = datetime.now() + timedelta(minutes=time_expire_token)
        encoded_token = jwt.encode(
            {'user_id': user_id, 'password': password},
            str(sms_code),
            algorithm='HS256')
        authSMS.token = encoded_token
        authSMS.state_SMS = state_SMS
        authSMS.save()
        return True,encoded_token
    except:
        return False



def decodeAndSaveStateSMS(token,authSMS):
    try:
        decode_token = jwt.decode(token, str(authSMS.codeSended), algorithms=["HS256"])
        authSMS.state_SMS = 4
        authSMS.save()
        return True
    except:
        return False