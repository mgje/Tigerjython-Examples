# Koch.py

from gturtle import *

def koch(s, n):
    if n == 0:
        forward(s)
        return
    koch(s / 3, n - 1)
    left(45)
    koch(s / 3, n - 1)
    right(90)
    koch(s / 3, n - 1)
    left(45)
    koch(s / 3, n - 1)

a = makeTurtle()
print dir(a)
a.setSize(900,900)
hideTurtle()
N = 4
L = 600
setPos( -240, 180)
right(90)
koch(L, N)
right(120)
koch(L, N)
right(120)
koch(L, N)
