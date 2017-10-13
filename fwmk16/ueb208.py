#Uebung 2.08

x0 = 1.0
x1 = 2.0

dx = 0.01

x= []

while x0 <= x1:
    x.append(x0)
    x0 += dx
    x0 = round (x0,2) # Korrktur Rundungsungenauigkeiten

print x