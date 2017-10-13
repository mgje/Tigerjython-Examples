#Uebung 2.10

l=[4,2,8,9,1,3,4]  # Input
N = len(l)         # Länge der Liste
out = []           # Output leere Liste
out.append(l)      # Unterste Schicht

while N > 1:
    l2 = []
    for i in range(N-1):
        tmp = l[i]+l[i+1]   # zwei Nachbarn  zusammenzählen
        l2.append(tmp)      # in die neue Liste einfügen
    
    out.append(l2)  # Neue Schicht hinzufügen
    l = l2          # Neue Schicht wird zur unteren Schicht
    N = len(l)      # Anzahl Elemente der neuen Schicht

print out
print out[-1][0]