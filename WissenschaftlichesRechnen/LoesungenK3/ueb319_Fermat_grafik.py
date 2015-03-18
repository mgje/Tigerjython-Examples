# Liste von Punkten in R2
from math import sqrt
from gpanel import *

def dist(P,Q):
    return sqrt((P[0]-Q[0])**2+(P[1]-Q[1])**2)


def schwerpunkt(punkte):
    n = len(punkte)
    x=y=0.0
    for P in punkte:
        x = x + P[0]
        y = y + P[1]
    return [x/n,y/n]

def iterationsschritt(P,punkte):
    W=x=y=0.0
    for Q in punkte:
        d = dist(P,Q)
        tmp = 1.0/d
        W = W +tmp
        x = x +Q[0]*tmp
        y = y +Q[1]*tmp
    return [x/W,y/W]

def fermatpunkt(punkte,eps):
    P = schwerpunkt(punkte)
    while True:
        Q = iterationsschritt(P,punkte)
        if dist(P,Q)<eps:
            return Q
        P = Q


P1 = [1,2]
P2 = [2,1]
P3 = [4,5]
P4 = [1,4]
P5 = [5,2]

punktliste = [P1,P2,P3,P4,P5]

sp = schwerpunkt(punktliste)
fp =  fermatpunkt(punktliste,0.001)

print "should be " + str(P2)

makeGPanel(0,600,0,600)
bgColor("gray")
col = makeColor(48,48,48,168)
setColor(col)

for P in punktliste:
    move(P[0]*100,P[1]*100)
    fillCircle(7)

move(sp[0]*100,sp[1]*100)
col = makeColor(0,183,183)
setColor(col)
fillCircle(7)


move(fp[0]*100,fp[1]*100)
col = makeColor(183,183,0)
setColor(col)
fillCircle(7)


