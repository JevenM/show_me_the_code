import os
import glob
from PIL import Image

def thumbnail_pic(filepath):
    pics = glob.glob(r'*.jpg')
    for pic in pics:
        imgname = os.path.join(filepath, pic)
        img = Image.open(imgname)
        img.thumbnail((1136, 640))
        print(img.format, img.size, img.mode)
        img.save(imgname, 'JPEG')
    print('Done')

if __name__ == '__main__':
    path = '.'
    thumbnail_pic(path)
