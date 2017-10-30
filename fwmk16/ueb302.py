#Uebung 3.02


def summenformel(z):
    l = []
    s=0
    for i in range(1,z+1):
        s = s + 1/i**2
        l.append(s)
    return s,l
    
print summenformel(3)