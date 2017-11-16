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

def euklidDiv(a0,b0):
    a=a0
    b=b0
    l=[]
    while a*b!=0:
        if a < b:
            a,b = b,a
        r = a%b
        q = a//b
        print "a:",a,"= ",q," x ",b,"+ ",r
        l.append([q,b])
        a=r

    return a+b,l
### Hier beginnt das Programm       
a = 80
b = 40
gp=initGPanel(a,a)
draw_Grid(a+2,a-2)

g,l = euklidDiv(64,27)

print l
s=0
for el in l:
    for j in range(el[0]):
        e = s+el[1]
        s = e
        drawbar(s,e,18,1,"green")