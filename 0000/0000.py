from PIL import Image,ImageDraw,ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:\Windows\Fonts\SIMYOU.TTF', size=40)
    fillcolor = '#ff0000'
    width, height = img.size
    draw.text((width-40, 0), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')

if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image)

