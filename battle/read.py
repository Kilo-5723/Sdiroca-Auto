import screen.locate as scr
from PIL import ImageGrab
import random
from ctypes import windll

dc = windll.user32.GetDC(0)


def getpixel(pos):
    return windll.gdi32.GetPixel(dc, pos[0], pos[1])


left = 0.274
right = 0.722
up = 0.713
down = 0.847

white = (255, 255, 255)
black = (100, 100, 255)
gold = (255, 255, 100)


def distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])


def read_color(position, image):
    rgb = getpixel(scr.to_global_position(position))
    color = (rgb & 0xFF, rgb >> 8 & 0xFF, rgb >> 16 & 0xFF)
    dw = distance(color,white)
    db = distance(color,black)
    dg = distance(color,gold)
    if dw<db and dw<dg:
      return 0
    if db<dg:
      return 1
    return 2
    


def read_board():
    image = ImageGrab.grab()
    arr = []
    for i in range(2):
        arr.append([])
        for j in range(7):
            pos = (left*(6-j)/6+right*j/6, up*(1-i)/1+down*i/1)
            arr[-1].append(read_color(pos, image))
    return arr
