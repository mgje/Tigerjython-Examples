# Prim Algorithm 2
from gturtle import *
import time
neueecken=True
ecken=[]

def zeichneKante(A,B):
    #hideTurtle()
    penUp()
    moveTo(A[0],A[1])
    penDown()
    moveTo(B[0],B[1])
    
def zeichneEcke(A):
    penUp()
    moveTo(A[0],A[1])
    dot(22)

def calcdist(A,B):
    return (A[0]-B[0])**2+(A[1]-B[1])**2

def findekante(l):
    outi = -1
    outf = -1
    mind = 100000.4
    for i in l:
        z = ecken[i]
        for j in nodelist:
            w = ecken[j]
            d = calcdist(z,w)
            if d < mind:
                mind = d
                outf = j
                outi = i
    return outi,outf
# Beim MouseClick
def onMouseHit(x, y):
    if neueecken:
        ecken.append([x, y])
        zeichneEcke([x, y])
        print(x,y,len(ecken))     
            
makeTurtle(mouseHit = onMouseHit)
hideTurtle()

while len(ecken)<23:
     time.sleep(2)          
# no new vertices
neueecken = False
                           
# Liste der nicht verbundenen Ecken
nodelist = range(len(ecken))
kanten = []
besuchte = []
# Wähle den ersten Knoten
e = 0
nodelist.remove(0)
besuchte.append(0)

#Solange bis jede Ecke verbunden ist
while len(nodelist)>0:
    e,f = findekante(besuchte)
    nodelist.remove(f)
    besuchte.append(f)
    kanten.append([e,f])
    
# Zeichne Kanten
for k in kanten:
    zeichneKante(ecken[k[0]],ecken[k[1]])
