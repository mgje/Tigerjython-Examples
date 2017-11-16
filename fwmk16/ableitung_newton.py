from math import sin

def ableitung(f,x,h=0.00001):
      return (f(x+h)-f(x))/h
# Newton
# f(x+h)=f(x)+h*f'(x)=0, also h=-f(x)/f'(x)
def newton(f,x0):
    while abs(f(x0))>1e-15:
        x0+=-f(x0)/ableitung(f,x0)
    return x0

def f(x):
    return (x-3)**2-1

print("Newton: Nullstelle von f : x=",newton(f,0))
print("Newton: Nullstelle von f : x=",newton(f,5))
print("pi-Newton: pi=",newton(sin,3))