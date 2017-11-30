
def findeWeg(weg,cities,dist,tot):
    global minL,roundtrip
    for city in cities[weg[-1]]:
        nweg = weg[:]
        if city not in weg:
            nweg.append(city)
            dist = dist + cities[weg[-1]][city]
            if len(nweg)>tot-1:
                print nweg, dist
                if dist < minL:
                    minL = dist
                    roundtrip = weg
                    
            else:
                findeWeg(nweg,cities,dist,tot)

cities = {
        'A': {'D': 195, 'B': 86, 'C': 178, 'I': 180, 'K': 91},
        'B': {'A': 86, 'D': 107, 'E': 171, 'C': 123},
        'C': {'A': 178, 'B': 123, 'E': 170},
        'D': {'A': 195, 'B': 107, 'E': 210, 'F': 210, 'G': 135, 'H': 64},
        'E': {'D': 210, 'B': 171, 'C': 170, 'G': 230, 'F': 230},
        'F': {'E': 230, 'D': 210, 'G': 85},
        'G': {'F': 85, 'E': 230, 'D': 135, 'H': 67},
        'H': {'G': 67, 'D': 64, 'I': 191},
        'I': {'H': 191, 'A': 180, 'K': 85, 'J': 91},
        'J': {'I': 91, 'K': 120},
        'K': {'I': 120, 'J': 85, 'A': 91}
    }

minL = 100000  
roundtrip = []      
findeWeg(['A'],cities,0,11)
print "Minmaler Weg", roundtrip,minL