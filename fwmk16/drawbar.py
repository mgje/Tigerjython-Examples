# Draw Bar
from gpanel import *

# Hilfs-Funktionen
def initGPanel(a,b):
    gp=makeGPanel(-0.11*a, 1.05*a, -0.08*b, 1.02*b)
    title("go go")
    windowSize(a*30, b*30)
    return gp
    
def draw_Grid(a,b):
    lineWidth(0)
    setColor(makeColor(0.0, 0, 0.1))
    drawGrid(0, a,0, b,int(a/2),int(b/2))
    lineWidth(2)
    setColor(makeColor(0.9, 0, 0.1))

def drawbar(x1,x2,y,w,c="black"):
    setColor(c)
    A = [x1,y]
    B = [x2,y-w]
    fillRectangle(A, B)
    setColor("black")
    rectangle(A,B)


### Hier beginnt das Programm       
a = 30
b = 40
gp=initGPanel(a,a)
draw_Grid(a+2,a-2)

drawbar(4,20,4,1,"green")
drawbar(2,4,7,1,"purple")
drawbar(0,18,11,1,"yellow")

