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

makeGPanel(-1, 20, -1, 20)

# draw coordinate system
line(0, -1, 0, 20) # x axis
line(-1, 0, 20, 0) # y axis

x  = 0
while x < 50:
    y = collatz(x)/100
    if x == 0:
        move(x/100, y)
    else:
        draw(x/100, y)
    x = x + 1


         
        
