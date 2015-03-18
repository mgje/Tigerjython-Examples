from math import sqrt
#N = input("N")
N = 100
korb = []
sieb = [] #Erst werden alle Zahlen bis N gesammelt in dieser Liste

for i in range(2,N+1,1):
    sieb.append(i)

while sieb[0] <= sqrt(N):       #Test muss nur bis zur Wurzel von N ausgefuehrt werden
    for i in sieb[1:]:
        if  i%(sieb[0]) == 0:   #Test, welche Zahlen mit der ersten modulo gerechnet 0 ergibt => Teiler
            sieb.remove(i)      #falls mod 0 dann aus Liste loeschen, weil keine Primzahl
    korb.append(sieb[0])        #Erste Zahl wird immer eine Primzahl sein und wird in Korb verschoben
    del sieb[0]             
    
print korb + sieb               # Im Sieb sind nun alles Primzahlen verblieben, plus jene aus dem Korb welche bei Algorithmus verschoben wurden.
