def C(F):                   # von Fahrenheit in Grad
    C = 5./9*(F-32)
    return C
print C(100)

def F(C):                   # Umkehrfunktion
    return (9.0/5)*C + 32
print F(37.777)

c = 212             # beliebige Temperatur in C mit zweifacher Umrechnung
print C(F(c))

