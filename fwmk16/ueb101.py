#Uebung 1.2
eingabe = 10**9

# Konstante
h = 60*60
tag = 24 * h
jahr = 365 * tag

#Berechnungen
anzahljahre = eingabe//jahr # Anzahl Jahre
resttage = eingabe % jahr # Rest in Sekunden
anzahltage = resttage //tag # Anzahl Tage
reststunden = resttage % tag # Rest in Sekunden
anzahlstunden = reststunden // h # Anzahl Stunden
restminuten = reststunden % h # Rest in Sekunden
anzahlminuten = restminuten // 60 # Anzahl Minuten
sekunden = restminuten % 60 # Anzahl Sekunden

print """Es gibt %d Jahre %d Tage %d Stunden %d Minuten %d Sekunden
      """%(anzahljahre,anzahltage,anzahlstunden,anzahlminuten,sekunden) 
