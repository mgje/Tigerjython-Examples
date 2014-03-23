from math import sqrt
from gpanel import *

def pfadlaenge(P):
    L = 0.0
    for i in range(1,len(P)):
        L=L+sqrt((P[i][0]-P[i-1][0])**2+(P[i][1]-P[i-1][1])**2)
    return L    
    

print pfadlaenge([[0,0], [1,0],[1,2], [0,2]])


makeGPanel(-3,4, -3, 4)
drawGrid(-2.0, 3., -2., 3.,)


lineWidth(3)
setColor("red")
move(0,0)
draw(1,0)
draw(1,2)
draw(0,2)
