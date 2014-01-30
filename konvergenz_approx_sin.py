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

def calcpp(ping,pong,pos):
    return [ (i%ping==0)!=(i%pong==0)*1.0 for i in range(1,pos+1)]
    
def calcdir(ping,pong,pos):
    return (-1)**sum(calcpp(ping,pong,pos))

def pingpong(ping,pong,pos):
    return sum([calcdir(ping,pong,i) for i in range(pos)])

def pingpongfunction(ping,pong,n):
    return [pingpong(ping,pong,i) for i in range(1,n+1)]

def maxpingpong(ping,pong):
    N = kgV(ping,pong)
    l = sorted(pingpongfunction(ping,pong,N), reverse = True)
    k = int(round(0.04*N+1))
    tot = 0
    for e in l[0:k]:
        tot += e
    return 1.0*tot/k   

def approxsin(ping,pong,x):
    N = kgV(ping,pong)
    return pingpong(ping,pong,x/math.pi*N)

#print maxpingpong(9,10)

makeGPanel(-1,8, -2, 2)

# draw coordinate system
line(0, 0, 8, 0) # x axis
line(0, -2, 0, 2) # y axis

setColor("blue")
x=0
while x < 2*math.pi:
    y = math.sin(x)
    if x == 0:
        move(x, y)
    else:
        draw(x, y)
    x = x + 0.04

setColor("green")
ping = 7;
pong = 8;
amp = maxpingpong(ping,pong)
count = 0
err = 0.0
x=0
while x < 2*math.pi:
    y = approxsin(ping,pong,x)/amp
    count += 1
    err += (math.sin(x)-y)**2
    if x == 0:
        move(x, y)
    else:
        draw(x, y)
    x = x + 0.01

print "Error"
print ping,pong
print err/count




