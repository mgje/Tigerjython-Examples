from math import sin,pi
#Ableitung

def lin(x):
    return 3*x-4

def zweinull(x):
    return x**2-4

def ableitung(f,x0,delta=0.0001):
    tmp = (f(x0+delta)-f(x0))/delta
    return tmp

def newton(f,x0,delta=0.000000001):
    while abs(f(x0))>delta:
        x0= x0-f(x0)/ableitung(f,x0)
    return x0 

print ableitung(lin,7)

print ableitung(sin,0,0.00000001)

print lin(1.33333)

print newton(lin,0)
print newton(zweinull,-5)

print [[x,newton(zweinull,x)] for x in range(-10,10)]