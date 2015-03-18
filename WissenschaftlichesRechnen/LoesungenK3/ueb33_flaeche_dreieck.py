# x1 = input("x1")
# y1 = input("y1")
# x2 = input("x2")
# y2 = input("y2")
# x3 = input("x3")
# y3 = input("y3")
x1 =0
y1 =0
x2 =4
y2 =0
x3 =0 
y3 =7


vektoren =[[x1,y1],[x2,y2],[x3,y3]]
print vektoren

def flaeche(vektoren):
    A = 1.0/2 * abs(vektoren[1][0]*vektoren[2][1]-vektoren[2][0]*vektoren[1][1]+vektoren[0][0]*vektoren[2][1]+vektoren[2][0]*vektoren[0][1]+vektoren[0][0]*vektoren[1][1]-vektoren[1][0]*vektoren[0][1])
    return A

print "Die Flaeche des Dreiecks mit den obigen Koordinaten lautet:", flaeche(vektoren)
