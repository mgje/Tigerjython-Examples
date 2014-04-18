# Lothar Collatz 1937
# Kovergiert die Collatz Folge immer?
# Paul Erdös wagte sogar den in Fachkreisen bekannten Satz: „Mathematics is not yet ready for such problems.“
import math
from gpanel import *


def collatz(x):
    x = math.floor(x)
    n = 0
    while x > 1:
        n = n+ 1
        if x%2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        #print "x: ",x,"n: ",n
    return n

N_Max = 200
y_Max = 120

makeGPanel(-N_Max*0.15, N_Max*1.05, -y_Max*0.12, y_Max*1.02)
drawGrid(0, N_Max, 0, y_Max)

lineWidth(1)
setColor("blue")


x  = 1
while x < N_Max:
    y = collatz(x)
    move(x, 0)
    draw(x, y)
    x = x + 1


         
        
