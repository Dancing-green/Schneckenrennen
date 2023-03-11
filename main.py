# PC soll auffordern Löwenzahn, Asphalt oder Fahrrad zu wählen. 
# Wenn gewählt, soll PC selbst zufälligt wählen, die Ergebnisse vergleichen (Asphalt schlägt Löwenzahn; Löwenzahn schlägt Fahrrad, Fahrrad schlägt Asphalt)
# PC soll Sieger*in bestimmen und ausgeben. Außerdem Punktestand speichern und neu abfragen

import random


print("Willkommen beim Schneckenrennen! Wähle Löwenzahn, Asphalt oder Fahrrad um deine Schnecke zu bewegen!")
Endergebnis = 0
while True:

    wahl = input("was möchtest du wählen? Löwenzahn, Asphalt oder Fahrrad?\n")

    valide_eingaben = ["Löwenzahn", "Asphalt", "Fahrrad", "Schneckenschleim"]
    valide_eingaben_pc = ["Löwenzahn", "Asphalt", "Fahrrad"]

    valide = False
    while valide is False:
        if wahl in valide_eingaben:
            valide = True
        else:
            wahl = input("Du doofes Schnecksche, mach nochmal!\n")

    print("du hast "+ wahl + " ausgewählt")
    pcwahl = random.choice(valide_eingaben_pc)
    print("Computer wählt " + pcwahl)

    if wahl == pcwahl :
        Ergebnis = 0
    if wahl == "Asphalt" and pcwahl == "Löwenzahn": 
        Ergebnis = -1
    if wahl == "Fahrrad" and pcwahl == "Löwenzahn":
        Ergebnis = 1
    if wahl == "Asphalt" and pcwahl == "Fahrrad":
        Ergebnis = -1
    if wahl == "Löwenzahn" and pcwahl == "Asphalt":
        Ergebnis = 1
    if wahl == "Löwenzahn" and pcwahl == "Fahrrad":
        Ergebnis = -1
    if wahl == "Fahrrad" and pcwahl == "Asphalt":
        Ergebnis = 1
    if wahl == "Schneckenschleim":
        Ergebnis = 0.5

    if Ergebnis > 0: 
        print("flottes Schneckchen!")
    if Ergebnis < 0:
        print("falsche Richtung!")
    if Ergebnis == 0:
        print("Lahme Schnecke!")
        
    Endergebnis += Ergebnis
    print("Deine Schnecke ist " + str(Endergebnis) + "cm vor der Computerschnecke")
