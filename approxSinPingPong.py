import math
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
    ping = 10
    pong = 11
    T = kgV(ping,pong)
    xMax = math.floor(T/2)
    yMax = calcPingPong(xMax,ping,pong)
    x_ = x/math.pi*T
    y = calcPingPong(x_,ping,pong)
    return 1.0/yMax*y


g=plotfunc(approxSin)
print dir(g)
print
print g

    


    



