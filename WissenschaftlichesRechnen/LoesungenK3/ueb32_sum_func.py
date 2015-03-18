def s(M):
    partsum = 0
    for k in range(1,M+1,1):
        partsum += 1.0/(k**2)  
    return partsum
print s(3)

