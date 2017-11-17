#Emily Murphy
#2017-11-17
#betterColoredWindow.py -
from random import randint
from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

whiteOutine = LineStyle(1, white)

blueRectangle = RectangleAsset(1500, 900, whiteOutine, blue)
greenRectangle = RectangleAsset(1500, 900, whiteOutine, green)
blackRectangle = RectangleAsset(1500, 900, whiteOutine, black)
redRectangle = RectangleAsset(1500, 900, whiteOutine, red)

windows = [blueRectangle,greenRectangle,blackRectangle,redRectangle]

def mouseClick(Event):
    num = randint(1,4)
    print(windows[num])

App().listenMouseEvent('click',mouseClick)
App().run()
