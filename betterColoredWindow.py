#Emily Murphy
#2017-11-17
#betterColoredWindow.py -
from random import randint
from ggame import *


colors = [Color(0xFF0000,1),Color(0x00FF00,1),Color(0x0000FF,1),Color(0x000000,1)]

def mouseClick(Event):
    num = randint(1,4)
    print(colors[num])

App().listenMouseEvent('click',mouseClick)
App().run()
