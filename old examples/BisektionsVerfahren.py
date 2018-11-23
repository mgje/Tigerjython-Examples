
def f(x):
    return x**3-3*x-0.5

def bisection(f,a,b,epsilon=(1.0e-4)):
    c = (a+b)/2.0
    while (b-a)/2.0 > epsilon:
        if f(c) == 0:
            return c
        elif f(a)*f(c) < 0:
            b = c
        else :
            a = c
        c = (a+b)/2.0      
    return c

def regula_falsi(f, a, b,epsilon=(1.0e-4)):
    c = 0.0
    while abs(f(c))>epsilon:
        c = b- (f(b)*((a-b)/(f(a)-f(b))))
        if f(b) > f(a):
            b = c
        else:
            a = c
    return c

print bisection(f,-2.5,-1.5)

print regula_falsi(f,-2.5,-1.5)
