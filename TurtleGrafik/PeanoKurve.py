# Peano.py

from gturtle import *

def peano(n, s, w):
    if n == 0:   
        return
    lt(w)
    peano(n - 1, s, -w)
    fd(s)
    rt(w)
    peano(n - 1, s, w)
    fd(s)
    peano(n - 1, s, w)
    rt(w)
    fd(s)
    peano(n - 1, s, -w)
    lt(w)
    
makeTurtle()
hideTurtle()
setPos(250, -250)
peano(4,30, 90)
