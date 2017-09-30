def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

def primefactors(n,l=[]):
    i = 2
    while(not (n % i ==0 and isPrime(i))and i<n):
        i = i+1
    neu = int(n/i)
    l.append(i)
    
    if neu > 1:
        primefactors(neu,l)
    
    return l

for i in range(1000000,1000030):
    print i, "  : ", primefactors(i,[])

