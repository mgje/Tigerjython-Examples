#Uebung 1.10
# Funktionen aus Mathebibliothek
from math import sqrt,exp, pi

# Eingabe
s=2
m=0
x=1

# Berechnung
y = 1/(sqrt(2*pi)*s)*exp(-1/2*((x-m)/s)**2)

# Ausgabe des Werts
print y