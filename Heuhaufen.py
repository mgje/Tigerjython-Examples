from gpanel import *
import random

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return makeColor(r, g, b,9)


makeGPanel(0, 20, 0, 20)

for i in range(30000):
    setColor(randomColor())
    line(random.random()*20,random.random()*20, random.random()*20, random.random()*20)
