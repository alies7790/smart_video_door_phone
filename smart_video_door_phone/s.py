# import requests
# pload = {
#   "mobile": "09215164458",
#   "password": "ali25ali25"
# }
# pload1 = {
#   "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWxpIiwicGFzc3dvcmQiOiJwYmtkZjJfc2hhMjU2JDI2MDAwMCRvM1lKUkYxU0FSRXdMTTRTYVU5aHpwJDR2RjZoQWxVK1hMOWNtUld0NXQvUUZzbnUvR2hkcy9tT1gxYjFFN3dlZU09In0.LNAjW1qO1fIk9V5m9LBJvOcRF6_bH_326oN68jFCIYE",
#   "sms_code": "123456"
# }
# # r = requests.post('http://127.0.0.1:8000/accounts/login-step1/',data = pload)
# r = requests.post('http://127.0.0.1:8000/accounts/login-step2/',data = pload1)
# print(r.text)
# print(r.cookies)


from PIL import Image

basewidth = 300
img = Image.open('rsz_120181122_162949.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('somepic.jpg')


import base64

with open("rsz_120181122_162949.jpg", "rb") as img_file:
    b64_string = base64.b64encode(img_file.read())
print(b64_string)

import numpy as np
import base64
import urllib
from PIL import Image


import base64
from PIL import Image
from io import BytesIO


im = Image.open(BytesIO(base64.b64decode(b64_string)))
im.save('image.png', 'PNG')