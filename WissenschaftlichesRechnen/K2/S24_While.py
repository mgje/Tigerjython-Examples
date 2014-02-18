print '------------------'
C = -20                             # Startwert von C
dC = 5                              # Erhöhung pro Durchlauf
while C <= 40:                      # Schleifenkopf
    F = (9.0/5)*C + 32              # 1. Anweisung in der Schleife 
    print C, F                      # 2. Anweisung in der Schleife
    C = C + dC                      # 3. Anweisung in der Schleife
print '------------------'
