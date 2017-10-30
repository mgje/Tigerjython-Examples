
def heron(a,e=0.000001):
    x=a
    y=1.0
    while abs(x**2-a)>e:
        x = (x+y)/2
        y = a/x
    return x

print heron(2)