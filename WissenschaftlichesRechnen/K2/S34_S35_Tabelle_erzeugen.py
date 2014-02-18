Cdegrees = range(-20, 41, 5) # -20, -15, ..., 35, 40 
Fdegrees = [0]*len(Cdegrees)
for i in range(len(Cdegrees)):
   Fdegrees[i] = (9.0/5)*Cdegrees[i] + 32
   
table = []
for C, F in zip(Cdegrees, Fdegrees):
     table.append([C, F])

print table
