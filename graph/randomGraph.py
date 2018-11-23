# Random Graph
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
    
    
makeTurtle()

ecken = [[0,0],[120,90],[-145,155],[130,-203],[-123,-130]]
kanten = [[0,1],[1,2],[2,4],[0,2],[0,4],[1,3]]

for e in ecken:
    zeichneEcke(e)

for k in kanten:
    zeichneKante(ecken[k[0]],ecken[k[1]])
    
hideTurtle()