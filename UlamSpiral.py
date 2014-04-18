import math
import time
from gpanel import *

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
k_Max = 800
N = math.floor(math.sqrt(k_Max+1/4)+0.5)
for i in range(1,N+1):
    for j in range(2):
        for k in range(i):
            ind = (2*(i-1)+j)%4
            weg.append(richtung[ind])   

N_G = int(math.floor(N/2))
gp = makeGPanel(-N_G*1.05, N_G*1.05, -N_G*1.149, N_G*1.05)
gp.windowSize(908, 908)
drawGrid(-N_G, N_G,-N_G, N_G,2*N_G,2*N_G)
font(Font("Courier", Font.BOLD, 42)) 

col1 = makeColor(233, 44, 3,255)
col2 = makeColor(22, 44, 3,255)
col3 = makeColor(222, 244, 3,255)
white = makeColor(255, 255, 255,255)
setColor(col1)
move(0,0)
fillCircle(0.45)


for k in range(1,k_Max):
    g = weg[0:k]
    a = [0,0]
    for b in g:
        a = map(sum, zip(a,b))
    time.sleep(0.5)
    p = k+41
    if isprime(p):
        setColor(col2)
    else:
        setColor(col1)
    if isquad(p):
        setColor(col3)
    
    move(a)
    fillCircle(0.48)

    setColor(white)
    fillRectangle(-1.1*N_G,-1.02*N_G,1.1*N_G,-1.12*N_G)
    
    setColor(col2)
    text(0,-1.12*N_G,str(int(p)))
    title(str(int(p)))
    

# Frage Wie wählt man das N, wenn man die k-te Zahl
# einzeichnen möchte
# Summe aller Zahlen von 1 bis N
# 1/2 N(N+1) --> also für 10 --> 0.5 *10 * 11 = 55
# Inverse Rechnung
# 1/2 N(N+1) = 78 | gesucht ist N
# N^2 + N = 156
# N^2 + N + 1/4 = 625/4
# (N+1)^2 = 625/4
# 1/2 N(N+1) = k
# (N+1)^2 = 2k+1/4
# N = sqrt(2k+1/4)-1
# Bei der Spirale werden zweimal alle Zahlen gezählt
# deshalb N = math.floor(math.sqrt(k+1/4))


