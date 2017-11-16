from math import log,exp
def sums(x0,q,n):
    s = 0
    l = []
    for i in range(n+1):
        seg = x0*q**i
        s += seg
        l.append(seg)
    return s,l


## Unterteile ein Strecke

l = 200 #mm
a = 5
e = 30

n = 13



q = exp(log(6)/n)
calcs,l = sums(a,q,n)
print "n",n
print "q",q
print l
print "tot",calcs




print q
