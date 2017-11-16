from math import sin,pi

# Integral
def quadf(x):
    return x**2

def f2(x):
    return x**3-x**2

def integral(f,a,b,N=100):
    delta = (b-a)/N
    s=0.0
    for i in range(N):
        tmp= delta*(f(a+i*delta)+f(a+(i+1)*delta))/2
        s = s + tmp
    return s

print integral(quadf,0,1,10000)
print integral(sin,0,pi,10000)
print integral(f2,-6,-5)