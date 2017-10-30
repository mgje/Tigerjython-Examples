def herondim(a,d,e=0.00001):
    x=a           # Start d-1 die Länge a
    y=a/x**(d-1)  # wähle y so das y * x^(d-1) = a ist
    while abs(x**d-a)>e: # solange der Unterschied grösser e
        x = (x*(d-1)+y)/d # das neue x Mittelwert aller Kanten 
        y = a/x**(d-1) # Volumen durch x^(d-1)
    return x

z = 987654
d = 13
w = herondim(z,d)

print "%.6f hoch %d ist %.6f"%(w,d,z)
