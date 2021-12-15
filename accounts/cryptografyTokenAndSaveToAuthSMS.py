
from datetime import datetime, timedelta
import random

import jwt


def encodeAndSaveToken(user_id,password,sms_code,authSMS,state_SMS,time_expire_token):
    try:
        dt = datetime.now() + timedelta(minutes=time_expire_token)
        rand_int = random.randint(10000000000000, 99999999999999)
        encoded_token = jwt.encode(
            {'user_id': user_id, 'rand_int': rand_int},
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
        return True
    except:
        return False