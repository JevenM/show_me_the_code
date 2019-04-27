import os
import re
import urllib
from urllib import request
from urllib.request import urlopen

def read_url(original_url):
    req = request.Request(original_url)
    req.add_header('User-Agent', ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36')
    with request.urlopen(req) as f:
        Imageurl(f.read().decode('utf-8'))
    return 0

def Imageurl(data):
    re_Imageurl = re.compile(r'src="(http://imgsrc.baidu.com/forum/.*?)"')
    data = re_Imageurl.findall(data)
    downloadImage(data)

def downloadImage(pic_url):
    dirct = '0013_pic'
    try:
        if not os.path.exists(dirct):
            os.mkdir(dirct)
    except:
        print('Failed to create directory in %s' % dirct)
        exit()
    for i in pic_url:
        data = urllib.request.urlopen(i).read()
        i = re.split('/', i)[-1]
        print(i)
        path = dirct + '/' + i
        f = open(path, 'wb')
        f.write(data)
        f.close()
    print('Done!')

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/4592201947'
    read_url(url)

