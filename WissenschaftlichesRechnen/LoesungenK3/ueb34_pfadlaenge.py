from math import sqrt
#eingabe = list(input("Gegen Sie die Koordinanten aller Punkte nach folgender Struktur ein: x1,y1,x2,y2,...yn,yn"))

eingabe =[0,0,3,0,4,1,0,3]
x =0
y =1
punkte =[]
h = 0
while h <= 0.5*len(eingabe)-1:
    punkte.append([eingabe[x],eingabe[y]])
    x += 2
    y += 2
    h += 1
print punkte

def pfadlaenge(punkte):
    s = 0
    for i in range(1,len(punkte),1):
        s += sqrt((punkte[i][0]-punkte[i-1][0])**2 + (punkte[i][1]-punkte[i-1][1])**2)
    return s
print "Die Pfadlaenge aufgrund obiger Punkte:", pfadlaenge(punkte)
        
