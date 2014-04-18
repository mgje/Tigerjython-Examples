
def f(x):
    return x**3-3*x-0.5

def ableit(f,x,h=0.01):
    return(f(x+h)-f(x-h))/(2*h)

def newton(f,x,epsilon=(1.0e-4)):
    while ( abs(f(x))>epsilon ) :
        x1 = x - f(x)/ableit(f,x)
        x = x1
    return x

print newton(f,0.5)
