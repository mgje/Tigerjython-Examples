# Euklid Visualization
from gpanel import *

# Hilfs-Funktionen
def initGPanel(N):
    makeGPanel(-10, N+2, -5, N+2)
    title("go go")
    windowSize(980, 900)
    


def draw_Grid(N):
    lineWidth(0)
    setColor(makeColor(0.0, 0, 0.1))
    drawGrid(0, N,0, N,20,20)
    lineWidth(3)
    setColor(makeColor(0.9, 0, 0.1))

def draw_Quads(A,B,b,i):
    setColor(makeColor(0.8, 0, 0.2+i*0.2))
    rectangle(A[0],A[1],B[0],B[1])


def euklid(a, b):
    i = 0
    A = [0,0] # Erste Ecke
    while b != 0:
        B = [A[0]+a,A[1]+b] # zweite Ecke
        draw_Quads(A,B,b,i)  
        a, b = b, a % b
        print i,a,b
        i += 1
    return a

### Hier beginnt das Programm
N = 100
initGPanel(N)
draw_Grid(N)
richtung = [[1,0],[0,1],[-1,0],[0,-1]]
ggt = euklid(96,52)
print ggt

