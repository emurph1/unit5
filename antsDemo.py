#Emily Murphy
#2017-11-20
#antsDemo.py - how to use lists with graphics
from random import randint
from ggame import *

WIDTH = 900
HEIGHT = 600

def step():
    for ant in data['antList']:
        dx = randint(-4,3)
        dy = randint(-4,3)
        if ant.x + dx > 0 and ant.x + dx < WIDTH:
            ant.x += dx
        if ant.y + dy > 0 and ant.y + dy < HEIGHT:
            ant.y += dy

if __name__ == '__main__':
    
    red = Color(0xFF0000,1)
    ant = CircleAsset(10,LineStyle(1,red),red)

    data = {}
    data['antList'] = []

    for i in range(50):
        data['antList'].append(Sprite(ant,(randint(1,WIDTH), randint(1,HEIGHT))))
    
    App().run(step)
