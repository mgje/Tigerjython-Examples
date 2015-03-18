
# Pi approximieren
# (c) Martin Guggisberg 2012

from math import pi

Ntot = 200000
z    = 1.0     
s    = 0.0
for n in range(Ntot):
    s = s + z / (2*n+1)
    z = z*(-1)            # Vorzeichen wechseln

print 'Pi approximiert mit %d Summanden ist %g'%(Ntot,s*4)
print 'Pi aus Math Bibliothek ist %g' % pi

