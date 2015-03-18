a = [1, 3, 5, 7, 11] 
b = [13, 17] 
c = a + b 
print c 
b[0] = -1 
d = [e+1 for e in a] # Alle Elemente in a werden um 1 erhoeht 
print d 
d.append(b[0] + 1) # Addiere 1 zu erstem Element in b --> -1 + 1 
d.append(b[-1] + 1) # Addiere 1 zu letztem Element in b --> 17 + 1 
print d[-2:]
