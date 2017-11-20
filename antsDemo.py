#Emily Murphy
#2017-11-20
#antsDemo.py - how to use lists with graphics
from random import randint
from ggame import *

WIDTH = 800
HEIGHT = 400

if __name__ == '__main__':
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(10,LineStyle(1,red),red)

    data = {}
    data['antList'] = []

    for i in range(10):
        data['antList'].append(Sprite(ant,(randint(1,WIDTH), randint(1,HEIGHT))))
    
    App().run()
