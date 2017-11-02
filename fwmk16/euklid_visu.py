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
    L = []
    
    while a*b!=0:
        # a soll im grösser sein
        if a < b:
            b,a = a,b
        L.append(a)
        L.append(b)
        
        print "a:",a," b:",b
        if a >= b:
            a = a%b
        else:
            a,b = b%a,a
    L.append(a+b)
    L.append(a+b)
    return a+b,L

### Hier beginnt das Programm       
gp=initGPanel(48,20)



for l in range(7):
    for k in range(39):
        clear()
        s = "a = "+str(40+l)+"   b = "+str(1+k) 
        font(Font("Arial",Font.BOLD,72)) 
        text (5,13,s)
        #draw_Grid(41,38)
        g,L = euklidDiv(40+l,1+k)

        drawbar(0,L[0],10,1,"red")
    
        start = 0
        for i in range(0,len(L)-1,4):
            a = L[i]
            b = L[i+1]
            N = a//b
    
            for j in range(N):
                drawbar(start,start+b,8,1,makeColor(0.01, (0.99-i*0.07)%1, 0.08*i%1))
                start = start +b
        delay(1323)



