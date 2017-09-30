#Uebung 1.5
# Import aus Mathebiliothek
from math import pi, sqrt

# Eingabe 
N = 2**128
R = 6371*100
O = 4*pi*R**2

# Berechnung
a = int(N/O) #Anzahl pro m2

s = int(sqrt(a)) # Anzahl Spalten und Zeilen eines quadratischen Gitters

# Ausgabe
print "%d Objekte könnte in einem quadratischen Gitter anordnen"%a
print "bestehend aus %d Spalten und %d Zeilen"%(s,s)
print "weil %d x %d = %d"%(s,s,s**2)
print "Der Gitterabstand beträgt %g m."%(1.0/s)
print "Dies ist 1000 x kleiner als der Atomradius von 1.0e-10 m"