import requests

token =''
def getTokenSmsSend():
    global token
    try:
        url = 'https://RestfulSms.com/api/Token'
        headers = {'Content-Type': 'application/json'}
        body = {'UserApiKey': 'e5788345d42ddd24882a8e7', 'SecretKey': '415##Dlcs&58dsaw34ew'}
        response = requests.post(url, headers=headers, json=body)
    except:
        return False
    if (response.json()['IsSuccessful']):
        token=response.json()['TokenKey']
        return True
    else:
        return False


def sendSmS(text_sending,code_sending,mobile,flag):
    global token
    if token == '':
        getTokenSmsSend()
    try:
        url = 'https://restfulsms.com/api/MessageSend'
        headers = {'Content-Type': 'application/json', 'x-sms-ir-secure-token': token}
        body = {"Messages": [str(text_sending) + str(code_sending)], "MobileNumbers": mobile,
                "LineNumber": "30004603370615", "SendDateTime": "", "CanContinueInCaseOfError": "false"}
        response = requests.post(url, headers=headers, json=body)
    except:
        return False
    if response.json()['IsSuccessful'] :
        return True
    elif flag ==0:
        status_update_token=getTokenSmsSend()
        if status_update_token:
            sendSmS(text_sending,code_sending,mobile,1)
        else:
            return False
    else:
        return False
