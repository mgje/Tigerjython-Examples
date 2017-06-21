# 41 and more Ulam's Spiral - Numberphile
# https://www.youtube.com/watch?v=3K-12i0jclM
# n -> n^2 - n + 41
import math
import time
from gpanel import *

k_Max = 50000

someprime = [n*n-n+41 for n in range(250)]

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def isquad(n):
    '''check if integer n is a quad'''
    tmp = math.sqrt(n)
    if tmp-math.floor(tmp)<0.000001:
        return True
    else:
        return False

richtung = [[1,0],[0,1],[-1,0],[0,-1]]
weg = []
N = int(math.floor(math.sqrt(k_Max+1/4)+0.5))
for i in range(1,N+1):
    for j in range(2):
        for k in range(i):
            ind = (2*(i-1)+j)%4
            weg.append(richtung[ind])
            
N_G = int(math.floor(N/2))
gp = makeGPanel(-N_G*1.05, N_G*1.05, -N_G*1.05, N_G*1.05)
gp.windowSize(920, 920)

#setColor(randomColor())
col1 = makeColor(233, 44, 3,255)
col2 = makeColor(22, 44, 3,255)
col3 = makeColor(222, 244, 3,255)
col4 = makeColor(2, 88, 254,255)
setColor(col1)
move(0,0)
fillRectangle(1,1)


for k in range(1,k_Max):
    g = weg[0:k]
    a = [0,0]
    for b in g:
        a = map(sum, zip(a,b))
    #time.sleep(0.01)
    p = k+41 
    setColor(col1)

    #if isquad(p):
    #    setColor(col3)

    if p in someprime:
        setColor(col4)

    if isprime(p):
        setColor(col2)
    
    move(a)
    fillRectangle(1,1)





