# Euklid Visualization
from gpanel import *

# Hilfs-Funktionen
def initGPanel(a,b):
    gp=makeGPanel(-0.11*a, 1.05*a, -0.08*b, 1.02*b)
    title("go go")
    windowSize(a*10, b*10)
    return gp
    
def draw_Grid(a,b):
    lineWidth(0)
    setColor(makeColor(0.0, 0, 0.1))
    drawGrid(0, a,0, b,int(a/10),int(b/10))
    lineWidth(2)
    setColor(makeColor(0.9, 0, 0.1))

def drawbar(x1,x2,y,w,c="black"):
    setColor(c)
    A = [x1,y]
    B = [x2,y-w]
    fillRectangle(A, B)
    setColor("black")
    rectangle(A,B)

def visuGgt(L):
    start = 0
    # draw a red
    drawbar(start,start+L[0],44,2,"red")
    for j in range(0,len(L)-1,2): # step 2
        a = L[j]
        b = L[j+1]
        n = a//b  # calc segments
        for i in range(n):
            drawbar(start,start+b,40,2,"yellow")
            start = start+b
                   
def euklid(a, b):
    i = 0
    L =[a]
    
    while b != 0:
        a, b = b, a % b
        L.append(a) 
        print i,a,b 
        i += 1
    L.append(a)
    return a,L


### Hier beginnt das Programm       
a = 84
b = 6
gp=initGPanel(a+4,a-10)
draw_Grid(a+2,a-8)
ggt,L = euklid(a,b)
print L
visuGgt(L)


# Loop 
for i in range(77):
    clear()
    #draw_Grid(a+2,a-8)
    s = "a = "+str(a)+"   b = "+str(b+i) 
    font(Font("Arial",Font.BOLD,72)) 
    text (8,30,s)
    ggt,L = euklid(a,b+i)
    visuGgt(L)
    delay(400)

    
    


    
