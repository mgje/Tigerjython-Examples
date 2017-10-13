#Uebung 2.05

s=0; k=1; M=100 

l=[]
while k < M:
    l.append(1.0/k) 
    k = k+1 ## Diese Zeile erhöht die Variable k

print l
print sum(l)