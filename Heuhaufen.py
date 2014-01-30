from gpanel import *
import random

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 22)
    return makeColor(r, g, b,9)


makeGPanel(0, 35, 0, 25)

for i in range(30000):
    setColor(randomColor())
    line(random.random()*35,random.random()*25, random.random()*35, random.random()*25)
