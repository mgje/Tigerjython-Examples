# ESR Prüfziffer berechnen
def calc_ESR_ziffer(nr):
    refn = nr.replace(" ", "")
    L = [int(i) for i in refn] # Liste aus Ziffern erzeugen
    L.pop()         # Hinterste Ziffer (Prüfziffer) entfernen
    l = len(L)      # Anzahl Ziffern
    c = 0           # Uebertrag (engl. carry) am Anfang
    
    # Schweizer Code Tabelle
    tabelle =  [0, 9, 4, 6, 8, 2, 7, 1, 3, 5]; 
    for i in range(l):          # Schleife über alle Ziffern von links nach rechts
        indx = (c + L[i])%10    # Berechnung indx (Uebertrag + Ziffer ) modulo 10 
        c = tabelle[indx]       # Uebertrag aus Tabelle
    res = 10 - c                # Prüfziffer 10 - letzter Übertrag
    return res

#refnr = "21 57030 00075 20033 45590 00126"
#refnr = "11 27098 76540 00000 55555 22228"
# Beispiel Post Finance
refnr = "3139471430009018"
print calc_ESR_ziffer(refnr)
