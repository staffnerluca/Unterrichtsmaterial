import random

liste = ["Kopf", "Zahl"]

anzahl_kopf = 0
anzahl_zahl = 0

weiter = True
while weiter:
    ergebnis = random.choice(liste)
    if ergebnis == "Kopf":
        anzahl_kopf += 1
    else:
        anzahl_zahl += 1
    print(ergebnis)
    nutzer_eingabe = input("Gib ende ein, wenn du nicht weiter machen willst: ")
    if nutzer_eingabe == "ende":
        weiter = False
print("Anzahl Kopf: " + str(anzahl_kopf))
print("Anzahl Zahl: " + str(anzahl_zahl))
# Einfaches Kopf oder Zahl, wird so lange ausgeführt bis der Nutzer sagt, dass er nicht mehr will
# gib am Ende die Anzahl von Kopf und von Zahl aus
