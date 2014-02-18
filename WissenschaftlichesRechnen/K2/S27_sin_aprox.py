x = 1.2    # x Wert für sin(x)
N = 25     # Maximale Ordnung
k = 1      # Zähler über die ungeraden Zahlen 1,3,5, ...
s = x      # Der erste Summand wird gleich zugeornet
sign = 1.0 

import math

while k < N:
      sign = - sign
      k=k+2
      term = sign*x**k/math.factorial(k) 
      s = s + term

print 'sin(%g) = %.16f (angenähert bis Ordnung %d )' % (x, s, N)

print 'sin(%g) = %.16f (Funktion aus Math lib)' %(x,math.sin(x))
