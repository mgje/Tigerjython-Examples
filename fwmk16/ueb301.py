#Uebung 3.01

def F(C):
    res = 9.0 / 5.0*C+32
    return res

def C(F):
    res = (F-32)/9.0*5.0
    return res

print F(10)
print "10 Grad C sind %.2f Grad F"% F(10)

print C(F(3423))