from gpanel import *
from time import *
import random
import math

#History
history = []
strength = 48.0

def dist(A,B):
    tmp = (A[0]-B[0])*(A[0]-B[0])+(A[1]-B[1])*(A[1]-B[1])
    return math.sqrt(tmp)

def mouseCallback(e):
    #global history
    global history
    if history is None:
        history = []
    
    x = toWindowX(e.getX())
    y = toWindowY(e.getY())
    P = [x,y]
    history.append(P)
    l = len(history)
    print l
    for i in range(l):
        Q = history[i]
        d = dist(P,Q)
        chance = 1*(l-i)/l+d/strength
        if (chance < random.random()*0.3):
            line(Q[0],Q[1],P[0],P[1])
        
                        
screenWidth = 60
screenHeight = 40

makeGPanel(0, screenWidth, 0, screenHeight, mouseDragged = mouseCallback)

# Green Screen
setColor(makeColor(182, 222, 217))
fillRectangle(0,0,screenWidth,screenHeight)
lineWidth(1);
# Alpha Chanel of black pen
setColor(makeColor(0, 0, 0, 9))







