from gpanel import *
from random import *

def randomColor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return makeColor(r, g, b,15)
    
makeGPanel(-3,4, -3, 4)
#drawGrid(-2.0, 3., -2., 3.,)

lineWidth(3)
setColor("red")

x = [0.5,-1.5,2.5,  3,   1,  -1,0]
y = [2.5,1.5, -1.0, -2.0,0.0,1, 0.5]

N = 100000

x = []
y = []
for i in range(N):
    r1 = random()*5-2
    r2 = random()*5-2
    x.append(r1)
    y.append(r2)


move(x[0],y[0])
for i in range(len(x)):
    setColor(randomColor())
    draw(x[i],y[i])


