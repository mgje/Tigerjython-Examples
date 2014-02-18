from math import sinh , exp , e , pi 

x = 2*pi

r1 = sinh(x)
r2 = 0.5*(exp(x)- exp(-x))
r3 = 0.5*(e**x-e**(-x)) 

print r1, r2, r3

print '%.16f %.16f %.16f' % (r1,r2,r3)

print '%.16f %.16f' % (1/49.0*49 , 1/51.0*51)

