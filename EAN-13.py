# ean-13 Code

def calc_ean_ziffer(code):
    L = [int(i) for i in str(code)] # Liste aus Ziffern
    L.pop() # Letzte Ziffer weg nehmen
    mul = 1 # Erste Faktor ist 1
    s = 0   # Summe auf 0 setzen
    l = len(L) # Anzahl Ziffern
    for i in range(l): # Schleife über alle Ziffern von Links nach rechts
        s = s + mul*L[i] # Erste Ziffer hat den Index l-1
        if (mul == 3): # Faktor wechseln 1 -> 3 oder 3 -> 1
            mul = 1
        else:
            mul = 3
    res = 10 - s%10 # Prüfuziffer ist 10 - Summe modulo 10
    return res # Prüfziffer zurück geben
        
        
code = 9783938802052
print calc_ean_ziffer(code)





