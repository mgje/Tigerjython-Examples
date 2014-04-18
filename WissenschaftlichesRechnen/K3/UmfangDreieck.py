from math import *
#Berechnung des Umfangs eines Dreiecks

def umfang(l):
    N = len(l)/2
    um = 0.0
    for i in range(N-1):
        quad =  sqrt((l[2*i]  -l[2*(i+1)])**2\\
               +(l[2*i+1]-l[2*(i+1)+1])**2)
        um += quad
        print um
    
    quad =  sqrt((l[0]  -l[-2])**2\\
               +(l[1]   -l[-1])**2)
    um += quad           
    return um
        
# Test mit Parametern (1,0) (3,0) (3,2)
print umfang([1.,0.,3.,0.,3.,2.,0.,0.])
