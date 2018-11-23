# Euklid Visualization
from gpanel import *

# Hilfs-Funktionen
def initGPanel(N):
    makeGPanel(-10, N+2, -5, N+2)
    title("go go")
    windowSize(980, 900)

def vadd(x,y):
    return [x[0]+y[0],x[1]+y[1]]

def proj(x,y):
    return [x[0]*y[0],x[1]*y[1]]

def length_width(A,B):
    x = abs(A[0]-B[0])
    y = abs(A[1]-B[1])
    if x > y:
        return x,y
    else:
        return y,x

def drawRect(A,B):
    rectangle(A[0],A[1],B[0],B[1])

def draw_Grid(N):
    lineWidth(1)
    setColor(makeColor(0.0, 0, 0.1))
    drawGrid(0, N,0, N,20,20)
    lineWidth(3)
    setColor(makeColor(0.9, 0, 0.1))

## A left lower corner
## B right upper corner
## i index 
def draw_Quads(A,B,i):
    setColor(makeColor(0.6, 0, 0.1+i*0.1)) 
    drawRect(A,B)
    l,b = length_width(A,B)
    C = [0,0]   #corner of the square
    C[0]=A[0]+b
    C[1]=A[1]+b 
    D = proj([b,b],richtung[i%2]) # stepdirection
    anz = int(l/b)
    for i in range(anz):
        drawRect(A,C)
        A = vadd(A,D)
        C = vadd(C,D)
    return A
    
def euklid(a, b):
    i = 0
    A = [0,0] # first corner left lower
    v = [a,b]
    B = vadd(A,v) # second corner upper right
    while b != 0:
        A = draw_Quads(A,B,i)  
        a, b = b, a % b
        print i,a,b
        i += 1
    return a

### Main
N = 100
initGPanel(N)
draw_Grid(N)
richtung = [[1,0],[0,1]]
ggt = euklid(101,64)
print ggt

### PlayGround
for i in range(99):
    clear()
    #draw_Grid(N)
    s = "a = "+str(101)+"   b = "+str(1+i) 
    font(Font("Arial",Font.BOLD,72)) 
    text (8,80,s)
    ggt = euklid(101,1+i)
    delay(700) 
    

