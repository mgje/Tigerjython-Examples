# Random Graph
from gturtle import *
from random import randint

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

N = 15
k = 37

ecken = []
for i in range(N):
    x = randint(-200,200)
    y = randint(-200,200)
    ecken.append([x,y])

kanten = []
for i in range(k):
    j = randint(0,N-1)
    p = randint(0,N-1)
    kanten.append([j,p])
    
for e in ecken:
    zeichneEcke(e)

hideTurtle()
for k in kanten:
    zeichneKante(ecken[k[0]],ecken[k[1]])
    
hideTurtle()