from PIL import Image, ImageFilter

im = Image.open('11-46-59-code.jpg')
im2 = im.filter(ImageFilter.SHARPEN)
im2.save('sharpen.jpg', 'jpeg')


