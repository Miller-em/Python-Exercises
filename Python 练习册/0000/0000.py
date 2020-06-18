from PIL import Image, ImageDraw, ImageFont
import random

def num_upprint(pic, num):
    image = Image.open(pic)         #打开图片
    draw = ImageDraw.Draw(image)    #创建draw对象
    x, y = image.size            #获取图片大小
    font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 40)   #加载字体
    fillcolor = "#ff0000"           #字体设置为红色
    draw.text((x-60, 40), "%s" % num, font = font, fill = fillcolor)    #添加字体位置，文字，字体颜色
    image.save("pic_get.jpg", "jpeg")

if __name__ == '__main__':
    pic = 'pic.jpg'
    num = random.randint(1, 10)
    num_upprint(pic, num)
