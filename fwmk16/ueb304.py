#Uebung 3.04

def dist(P,Q):
    res = (P[0]-Q[0])**2+(P[1]-Q[1])**2
    res2 = sqrt(res)
    return res2

def laengePfad(L):
    N = len(L)
    s = 0
    for i in range(N-1):
        s = s + dist(L[i],L[i+1])
    return s
    
#print dist([0,0],[1,1])

L = [[0,0], [1,0],[1,2], [0,2],[0,7],[7,7]]
print laengePfad(L)