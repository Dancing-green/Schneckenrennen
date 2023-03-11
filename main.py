# PC soll auffordern Schere, Stein oder Papier zu wählen. 
# Wenn gewählt, soll PC selbst zufälligt wählen, die Ergebnisse vergleichen (Stein schlägt Schere; Schere schlägt Papier, Papier schlägt Stein)
# PC soll Sieger*in bestimmen und ausgeben. Außerdem Punktestand speichern und neu abfragen

import random


print("Willkommen zum Spiel 'Schere, Stein, Papier'")
Endergebnis = 0
while True:

    wahl = input("was möchtest du wählen? Schere, Stein oder Papier?\n")

    valide_eingaben = ["Schere", "Stein", "Papier"]

    valide = False
    while valide is False:
        if wahl in valide_eingaben:
            valide = True
        else:
            wahl = input("Das nicht gut!1! Mach nochmal!\n")

    print("du hast "+ wahl + " ausgewählt")
    pcwahl = random.choice(valide_eingaben)
    print("Computer wählt " + pcwahl)

    if wahl == pcwahl :
        Ergebnis = 0
    if wahl == "Stein" and pcwahl == "Schere": 
        Ergebnis = 1
    if wahl == "Papier" and pcwahl == "Schere":
        Ergebnis = -1
    if wahl == "Stein" and pcwahl == "Papier":
        Ergebnis = -1
    if wahl == "Schere" and pcwahl == "Stein":
        Ergebnis = -1
    if wahl == "Schere" and pcwahl == "Papier":
        Ergebnis = 1
    if wahl == "Papier" and pcwahl == "Stein":
        Ergebnis = 1

    if Ergebnis > 0: 
        print("du hast gewonnen")
    if Ergebnis < 0:
        print("du Loser")
    if Ergebnis == 0:
        print("unentschieden")
        
    print(Ergebnis)
    Endergebnis += Ergebnis
    print("Der Zwischenstand beträgt " + str(Endergebnis))
