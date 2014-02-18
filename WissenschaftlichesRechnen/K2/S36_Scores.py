# Liste scores erstellen und mit Werten füllen
scores = []
scores.append([12, 16, 11, 12])                 # player no. 0
scores.append([9])                              # player no. 1 
scores.append([6, 9, 11, 14, 17, 15, 14, 20])   # player no. 2

# Ausgabe

for p in range(len(scores)):
    for g in range(len(scores[p])):
         score = scores[p][g]
         print '%4d' % score,
    print ''
