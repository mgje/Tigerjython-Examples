#Uebung 3.03

def flaeche(L):
    x1 = L[0][0]
    x2 = L[1][0]
    x3 = L[2][0]
    y1 = L[0][1]
    y2 = L[1][1]
    y3 = L[2][1]
    term = x2*y3-x3*y2-x1*y3+x3*y1+x1*y2+x2*y1
    A = 1/2*abs(term)
    return A

#   x1,y1 x2,y2 x3,y3
L= [[0,0],[1,0],[0,2]] 

#print L[0][0]
print flaeche(L)