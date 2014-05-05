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

makeTurtle()
hideTurtle()
N = 4
L = 200
setPos( -240, 180)
right(90)
koch(L, N)
right(120)
koch(L, N)
right(120)
koch(L, N)
