import os
from PIL import Image

def thumbnail_pic(a,b=1136, c=640):
    for x in a:
        if os.path.splitext(x)[-1] == ".jpg":
            name = os.path.join('.', x)
            im = Image.open(name)
            print('Before: ' + im.format, im.size, im.mode)
            im.thumbnail((b,c))
            print('After: ' + im.format, im.size, im.mode)
            im.save(name, 'JPEG')

a = os.listdir('.')
PHONE = {'iphone5':(1136,640), 'iphone6':(1134,750), 'iphone6P':(2208,1242)}
width, height = PHONE['iphone6']
thumbnail_pic(a, width, height)
