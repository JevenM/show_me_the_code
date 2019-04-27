# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import datetime

def randchar():
    return chr(random.randint(65, 90)) # 返回对应的ascii字符

def randcolor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def randcolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def generateJpg():
    # 四个字符
    width = 60 * 4
    height = 60
    # 创建图片
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建文字对象
    font = ImageFont.truetype('C:\\Windows\\Fonts\\REFSAN.TTF', 36)
    # 创建draw对象
    draw = ImageDraw.Draw(image)
    # 填充颜色
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=randcolor1())
    # 输出文字
    for t in range(4):
        draw.text((60 * t + 10, 10), randchar(), font=font, fill=randcolor1())
    # 增加模糊
    image = image.filter(ImageFilter.BLUR)
    # 文件命名
    time = datetime.datetime.now().strftime('%H-%M-%S')
    image.save(time+'-code.jpg', 'jpeg')

if __name__ == '__main__':
    generateJpg()
