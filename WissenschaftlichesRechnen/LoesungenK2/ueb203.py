
# Ungerade Nummern in einer Liste speichern
# (c) Martin Guggisberg 2012


n_max=99
n=21
l=[]

while (n<n_max):
    l.append(n)
    n = n + 2

print l

# Moeglichkeit 2
C=[]
count = 21
while (count < n_max): 
 C = C + [count] 
 count = count + 2 
 
print C 
