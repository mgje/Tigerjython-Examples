#Uebung 2.13

# Nullstellen
roots = [-1,1,2]
x = 1.4

y = 1   # Bei Produkten ist 1 das neutrale Element
for r in roots:
    y = y * (x-r)

print y
print (x+1)*(x-1)*(x-2)