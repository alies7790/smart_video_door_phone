
import base64
from PIL import Image
from io import BytesIO
from rest_framework.response import Response
from rest_framework import  status
def resizeImage(picture):
    try:
        img = Image.open(BytesIO(base64.b64decode(picture)))
    except:
        return False
    basewidth = 300
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    resize_picture = base64.b64encode(buffered.getvalue())
    return resize_picture