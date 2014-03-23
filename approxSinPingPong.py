import math
from gpanel import *

def ggT(a,b): # Rekursive Definition nach Euklid
    if a==b: return a
    if a==1 or b==1: return 1
    if a==0: return b
    if b==0: return a
    if a>b: return ggT(a%b,b)
    if a<b: return ggT(a,b%a)

def kgV(a,b):
    return a*b/ggT(a,b)

def teilt(a,b):
    if a%b==0:
        return True
    if b%a==0:
        return True
    return False

def calcPingPong(x,ping,pong):
    n = 1
    pos = 0
    direction = 1
    pingpong = kgV(ping,pong)
    
    while (n <= x):
        if n%pingpong==0:
            #do nothing
            pass
        elif n%ping==0 or n%pong==0:
            direction *= -1
        n += 1
        pos += direction
    return pos

def pFunc(x):
    return calcPingPong(x,4,3)

def approxSin(x):
    ping = 101
    pong = 102
    T = kgV(ping,pong)
    xMax = math.floor(T/2)
    yMax = calcPingPong(xMax,ping,pong)
    x_ = x/math.pi*T
    y = calcPingPong(x_,ping,pong)
    return 1.0/yMax*y


#g=plotfunc(approxSin)
#lk = dir(g)
#for e in lk:

#    print e,type(e)
#print
#print g

makeGPanel(-1, 11, -3, 3)
drawGrid(0, 10, -2.0, 2.0)


x  = 0
while x < 10:
    y = approxSin(x)
    if x == 0:
        move(x, y)
    else:
        draw(x, y)
    x = x + 0.001

    


    



