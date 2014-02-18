n = 21
C_min = -10
C_max = 40
dC = (C_max - C_min)/float(n-1) # increment in C
  
Cdegrees = [0]*n
for i in range(len(Cdegrees)):
       Cdegrees[i] = -10 + i*dC
  
Fdegrees = [0]*n
for i in range(len(Cdegrees)):
   Fdegrees[i] = (9.0/5)*Cdegrees[i] + 32
   
for i in range(len(Cdegrees)):
   print '%5.1f %5.1f' % (Cdegrees[i], Fdegrees[i])
