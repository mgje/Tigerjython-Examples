#Uebung 1.4
# pi aus der Mathebibliothek importieren
from math import pi

# Eingabe
N = 2**128
R = 6371*100


# Berechnung
O = 4*pi*R**2
anz = N/O

# Ausgabe
print "Es gibt %d Adressen pro m2"%anz