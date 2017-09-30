#Uebung 2.01

#F=9.0/5∗C+32; umkehren

print "F  \t| \tC"

F = 0.0
while F < 100: 
    C = (F - 32)*5.0/9.0
    print "%.2f  \t|\t%.2f"%(F,C)
    F = F + 10
    
