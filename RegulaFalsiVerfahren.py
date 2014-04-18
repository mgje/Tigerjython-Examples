
def f(x):
    return x**3-3*x-0.5

def regula_falsi(f, a, b,epsilon=(1.0e-4)):
    c = 0.0
    while abs(f(c))>epsilon:
        c = b- (f(b)*((a-b)/(f(a)-f(b))))
        if f(b) > f(a):
            b = c
        else:
            a = c
    return c

print regula_falsi(f,-2.5,-1.5)
