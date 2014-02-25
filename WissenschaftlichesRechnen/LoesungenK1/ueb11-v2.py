from math import e, pi

i = complex(0,1)

z1= 2*e**(pi/6*i)
z2= 2*e**(2*pi/3*i)
z3= 4*e**(pi/4*(-i))

print "Komplexe Zahl: %03f+%03fi"%(z1.real,z1.imag)

print "Komplexe Zahl: %03f+%03fi"%(z2.real,z2.imag)

print "Komplexe Zahl: %03f+%03fi"%(z3.real,z3.imag)
