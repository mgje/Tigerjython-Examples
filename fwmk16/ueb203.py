#Uebung 2.03

# Konstante
v0 = 1
g = 9.81
n = 11
T = 2*v0/g  #Zeitintervall das betrachtet wird
dt = T/(n-1)    #Zeitschritt

i = 0 # Start Index
t =0 # Start Zeit
print"Zeit t \t| \tHöhe y"
# Schleife
while i < n:
    y = v0*t-0.5*g*t**2
    print"%.3f \t| \t%.3f"%(t,y)
    i = i +1
    t = t +dt