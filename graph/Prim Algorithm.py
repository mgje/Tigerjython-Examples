# Prim Algorithm
from gturtle import *

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
    
makeTurtle()
hideTurtle()

# Define verticies
ecken = [[0,0],[120,90],[-145,155],[130,-203],[-123,-130],
         [30,60],[-220,30],[-100,90],[130,-73],[30,-90]]
         
# Liste der nicht verbundenen Ecken
nodelist = range(len(ecken))

# Draw Graph
for e in ecken:
    zeichneEcke(e)

graph = []
besuchte = []
# Wähle den ersten Knoten
e = 0
nodelist.remove(0)
besuchte.append(0)

# Kantenliste
kanten = []

while len(nodelist)>0:
    e,f = findekante(besuchte)
    nodelist.remove(f)
    besuchte.append(f)
    kanten.append([e,f])
    
# Zeichne Kanten
for k in kanten:
    zeichneKante(ecken[k[0]],ecken[k[1]])
        
hideTurtle()