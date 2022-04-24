from random import randint
import os
from PIL import Image, ImageDraw
 
def circles_generator(num_of_circles, radius):

    if not os.path.exists('circles'):
        os.mkdir('circles')

    for pic_name in range(1, num_of_circles + 1):
        img = Image.new('RGB', (radius, radius), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.ellipse((0, 0, radius, radius), fill=(randint(0, 255), randint(0, 255), randint(0, 255)))
        img.save(f'circles/{pic_name}.jpg', quality=85)
 
try:
    number = int(input('Введите количество: ')) 
    rad= int(input('Введите радиус: '))
    circles_generator(number,rad)
except: print('Не правильный формат данных')