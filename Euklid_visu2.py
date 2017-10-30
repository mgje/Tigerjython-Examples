# Euklid Visualization
from gpanel import *

def initDisplay(N):
    #N_G = int(math.floor(N/2))
    makeGPanel(-N*0.1, N*1.01, -0.1*N, N*1.01)
    title("go go")
    windowSize(980, 900)
    drawGrid(0, N,0, N,20,20)
    
    lineWidth(3)
    setColor(makeColor(0.8, 0, 0.2))
    #line(0,0,3,3) 
    #rectangle(0,0,10,100)   

def euklid(a, b):
    xp=0
    yp=0
    i = 0
    
    #           1            2                3            4                 5             6               7                8              
    M = [[[1,0],[0,1]],[[0,1],[1,0]],[[-1,0],[0,1]],[[0,-1],[-1,0]],[[0,-1],[-1,0]],[[1,0],[0,-1]],[[1,0],[0,-1]],[[0,1],[1,0]],[[1,0],[0,-1]],[[1,0],[0,-1]]]
    N = [[[1,0],[0,0]],[[0,1],[1,0]],[[-1,0],[0,1]],[[0,-1],[0,0]],[[0,-1],[-1,0]],[[0,0],[0,-1]],[[1,0],[0,-1]], [[0,1],[1,0]],[[0,0],[0,-1]],[[1,0],[0,-1]]]
    
    
    while b != 0:
        setColor(makeColor(0.8-i*0.08, 0, 0.2+i*0.1))
        x2 = xp+M[i][0][0]*a+M[i][0][1]*b
        y2 = yp+M[i][1][0]*a+M[i][1][1]*b
        rectangle(xp,yp,x2,y2) 
        xp = xp+N[i][0][0]*a+N[i][0][1]*b
        yp = yp+N[i][1][0]*a+N[i][1][1]*b 
        move(xp,yp)
        circle(2);
        a, b = b, a % b
        print i,a,b
        
        i += 1
    return a

N = 300
initDisplay(N)
for i in range(1):
    ggt = euklid(194,120)
    print ggt
    input("enter")
    clear()
    setColor(makeColor(0.0, 0, 0.0))
    lineWidth(1)
    drawGrid(0, N,0, N,20,20)
    lineWidth(3)

