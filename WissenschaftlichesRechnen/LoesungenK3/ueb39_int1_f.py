from math import sin, cos, sqrt
k = 1000000

def quad(x):
	return x*x

def norm(x):                
    return sqrt(x*x)
    
def integral1(f,a,b):
    dx = float(b-a)/k
    x = a
    summe = 0.0
    while x <= b:
        summe += f(x)*dx
        x += dx
    return summe

print integral1(norm,1,5)
print integral1(quad,0,3)

