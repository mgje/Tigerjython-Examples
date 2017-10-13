#Uebung 2.11
import itertools
perm = itertools.permutations([2, 3, 5, 6, 7, 8, 9])

permlist = [ e for e in perm]
print "" ,len(permlist), " Permutationen"

mperm = []
max = 0

for l in permlist:
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

    if max < out[-1][0]:
        max = out[-1][0]
        mperm = out[0]

print "Der maximale Wert ist ",max
print "Das Fundament dieser Zahlenmauer ist ", list(mperm)