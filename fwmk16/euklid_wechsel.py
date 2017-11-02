# Euklid nach Matlab Prog aus Artikel

def EuklidSub(a0,b0):
    a = a0
    b = b0
    while a*b!=0:
        print "a:",a," ","b:",b
        if a >= b:
            a = a-b
        else:
            b = b-a
    return a+b

print EuklidSub(65,5)