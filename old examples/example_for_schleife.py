from gturtle import *

def line(x1, y1, x2, y2):
    setPos(x1, y1)
    moveTo(x2, y2)

makeTurtle()
hideTurtle()

for i in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
    line(10 * i, 0, 200, 10 * i)