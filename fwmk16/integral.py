# Integral

def integral(f,a,b,n=10000):
# n Zahl der Streifen default ist 10000
    delta = (b - a)/n # Streifenbreite 
    s=0.0 # Summe
    for i in range(n):
            s=s+0.5*(f(a+i*delta)+f(a+(i+1)*delta))*delta
    return s

def quadf(x):
    return x**2

print integral(quadf,0,1,100)
