from math import cos, sin, pi, sqrt
k = 10      # je groesser k gewaehlt wird, umso genauer wird pi approximiert
            # bei k=20 ist eine kritische Grenze, welche das Prgm noch im Stande ist zu rechnen, nachher stuerzt die Sache ab. Wie kann ich den Algorithmus vereinfachen? bzw. wo genau muss ich ansetzen, um Rechenaufwand einzusparen?
N = 2**k
punkte = []
for i in range(0,N,1):
    punkte.append([0.5*cos(2*pi*i/N),0.5*sin(2*pi*i/N)])

def pfadlaenge(punkte):
    s = 0
    for i in range(1,len(punkte),1):
        s += sqrt((punkte[i][0]-punkte[i-1][0])**2 + (punkte[i][1]-punkte[i-1][1])**2)
    return s
print "Approximation der Zahl pi mit einem Polygon von N = 2^k, wobei k = %g : " %(k)
print pfadlaenge(punkte) 
print ""
print "Zahl pi zum Vergleich:"
print pi
