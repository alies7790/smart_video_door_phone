
import base64
from PIL import Image
from io import BytesIO
def resizeImage(picture):
    img = Image.open(BytesIO(base64.decodestring(picture)))
    basewidth = 400
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    resize_picture = base64.encodestring(buffered.getvalue())
    return resize_picture
