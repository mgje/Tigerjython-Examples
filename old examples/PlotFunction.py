import math
from gpanel import *

def makePlot(f,xmin=(-10.0),xmax=10.0,ymin=(-10.0),ymax=10.0, sampling=200, pencolor="blue"):
    if xmax < xmin:
        [xmax,xmin]=[xmin,xmax]
    if ymax < ymin:
        [ymax,ymin]=[ymin,ymax]

    xmin *= 1.0
    xmax *= 1.0
    ymin *= 1.0
    ymax *= 1.0
    
    lrand = (xmax-xmin)*0.15
    rrand = (xmax-xmin)*0.05
    orand = (ymax-ymin)*0.05
    urand = (ymax-ymin)*0.1
    makeGPanel(xmin-lrand,xmax+rrand,ymin-urand,ymax+orand)
    drawGrid(xmin,xmax,ymin,ymax)

    setColor(pencolor)
    dx = (xmax-xmin)/sampling
    x = xmin
    move (x,f(x))
    
    while x < xmax:
        y = f(x)
        draw(x, y)
        x = x + dx

def f(x):
    return (x-4)**2-6


makePlot(f,0,8,-10,10)
