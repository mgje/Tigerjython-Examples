
def neueStadt(cities,path):
    if len(cities)>1:
        for city in cities:
            cln = [c for c in cities if c != city]
            np = path[:]
            np.append(city)
            neueStadt(cln,np) 
    else:
        path.append(cities[0])
        s = ''.join(str(e)+"->" for e in path)
        s = s+path[0]
        print s

l = ["A","B","C","D"]
start = l.pop(0)
neueStadt(l,[start])