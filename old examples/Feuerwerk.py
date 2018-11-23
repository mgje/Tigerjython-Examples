from gpanel import *
from time import *
import random

mouseX=0
mouseY=0

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return makeColor(r, g, b)

def mouseCallback(e):
    #save MousePosition in global variable
    global mouseX,mouseY
    mouseX = toWindowX(e.getX())
    mouseY = toWindowY(e.getY())
                        

screenWidth = 60
screenHeight = 40

makeGPanel(0, screenWidth, 0, screenHeight, mouseMoved = mouseCallback)

# Black Screen
setColor(makeColor(0, 0, 0))
fillRectangle(0,0,screenWidth,screenHeight)
lineWidth(4);

# Frames do it every 0.01 second
while(True):
    setColor(randomColor())
    line(mouseX, mouseY, mouseX+(random.random()-0.5)*14, mouseY+(random.random()-0.5)*14)  
    sleep(0.01)
    setColor(makeColor(0, 0, 0,14))
    fillRectangle(0,0,screenWidth,screenHeight)




