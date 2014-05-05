# TreeFractal.py

from gturtle import *

def tree(size):
    if size < 5:
        fd(size)
        bk(size)
        return
      
    fd(size / 3)
    lt(30)
    tree(size * 2 / 3)
    rt(30)
    fd(size / 6)
    rt(25)
    tree(size / 2)
    lt(25)
    fd(size / 3)
    rt(25)
    tree(size / 2)
    lt(25)
    fd(size / 6)
    bk(size)

makeTurtle()
ht()
setPos(20, -195)
tree(250)
