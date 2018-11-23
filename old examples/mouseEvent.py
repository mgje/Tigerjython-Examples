from gturtle import *
import random

# create color palette
def make100col(r1,g1,b1,r2,g2,b2):
    cols = []
    for i in range(101):
        r = int(r1 + i * (r2-r1) / 100)
        g = int(g1 + i * (g2-g1) / 100)
        b = int(b1 + i * (b2-b1) / 100)
        cols.append((r,g,b))
    return cols

# is the turtle ot of the window
def outOfWindow():
    p = getPos()
    if p[0] > -400 and p[0] < 400:
        return False
    if p[1] > -300 and p[1] < 300:
        return False
    return True

# Mouse Click Event
def onMousePressed(x, y):
    for i in range(600):
        steps = random.randint(70,250)
        v = random.randint(0,100)
        setPenColor(makeColor(cols[v]))
        setRandomHeading()
        forward(steps)
        if outOfWindow():
            home()
            
# create color palette                   
cols = make100col(255,255,255,0,0,255)  
 
# start turtle world and register mouse event     
makeTurtle(mousePressed = onMousePressed)

# runs 1000x faster without turtle figure
hideTurtle()
setPenWidth(10)


