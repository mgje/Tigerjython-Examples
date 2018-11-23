from gturtle import *

makeTurtle()
hideTurtle()
setPos(-300, -200)

a = 1
while a < 100:
    delay(100)
    forward(8)
    right(a)
    a = 1.01*a