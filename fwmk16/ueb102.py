#Uebung 1.2
eingabe = 10*1000 # in Meter

#Berechnung
ainc = eingabe/0.0254 # Alles in Inches
afeet = ainc / 12 # Alles in Feet
ayards = afeet / 3 # Alles in Yards
amiles = ayards / 1760 # Alles in Miles
print "%g Meter sind %.3f Inches"%(eingabe,ainc)
print "%g Meter sind %g Feets"%(eingabe,afeet)
print "%g Meter sind %g Yards"%(eingabe,ayards)
print "%g Meter sind %g Meilen"%(eingabe,amiles)

## Hier folgt ein Zusatz
## Fuer eine gemischte Ausgabe muss jeweils mit Rest gerechnet werden.

## Berechung 
miles = int(amiles) # Meilen ganzzahliger Anteil
restyards = (amiles-miles)*1760 # Rest in Yards berechnen
yards = int(restyards)# ganzzahliger Anteil in yards
restfeets = (restyards-yards)*3 # Rest in Feets berechnen
feets = int(restfeets)# ganzzahliger Anteil in feets
inces = (restfeets-feets)*12 #Rest in inches mit Dezimalstellen
print """%g Meter sind %d Meilen %d Yards %d Feets %.3f Inches
      """%(eingabe,miles,yards,feets,inces)