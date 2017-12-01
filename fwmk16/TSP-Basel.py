cities = {
'A': {'D': 195, 'B': 86, 'C': 178},
'B': {'A': 86, 'D': 107,  'C': 123},
'C': {'A': 178, 'B': 123, 'D':200 },
'D': {'A': 195, 'B': 107, 'C': 200}
}


def finde_kuerzester(ort,moeg):
    dist = 10000000
    dest = ''
    for m in moeg:
        if cities[ort][m] < dist:
            dest = m
            dist = cities[ort][m]
    return dest
    
def moeglichkeiten(weg):
    ort = weg[-1]
    schonbesucht = weg[:-1]
    moeg=[ c for c in cities[ort] if c not in schonbesucht]
    return moeg

def rundreise(weg):
    ort = weg[-1]
    no = finde_kuerzester(ort,moeglichkeiten(weg))
    weg.append(no)
    if len(weg) > 3:
        print weg
    else:
        rundreise(weg) 
    

start = 'A'

rundreise([start])

