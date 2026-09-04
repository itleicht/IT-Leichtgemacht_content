# Folge 2: Die Maschine trifft eine Entscheidung
# Projekt: Ein regelbasierter Katze-oder-Hund-Klassifizierer

"""
    Datentypen, die wir bisher gelernt haben
    - Ganzzahlen
    - Kommazahlen
    - Zeichenketten
"""
number = 1 # Ganzzahl - Variable
print(type(number))
number2 = 3.14 # Kommazahlen - Variable
print(type(number2)) 
entry = "Das Wetter ist heute sehr heiß"
print(type(entry))

fur_length = input("Wie lang ist das Fell in cm (geschätzt)? ")
fur_length = float(fur_length)

weight = input("Wie schwer ist das Tier in kg ?")
weight = float(weight)


# Einfache Regeln: schwer und kurzes Fell -> eher Hund
# leicht und langes Fell -> eher Katze

# Vergleichsoperatoren
# print(3 > 5)
# print(3 < 5)
# print(3 == 5)
# print(3 != 5)
# print(3 >= 5)
# print(3 <= 5)

# and und or
# print(3 == 3 and 5 < 4) # Beide Bedingungen müssen True sein, damit der Gesamtausdruck True ist
# print(3 == 3 or 5 < 4) # Eine Bedingung oder beide müssen True sein, damit der Gesamtausdruck True ist

# if-Bedingungen
if weight > 8 and fur_length < 5:
    print("Das könnte ein Hund sein!")
elif weight <= 8 and fur_length >= 5:
    print("Das könnte eine Katze sein!")
else:
    print("Schwer zu sagen, was das sein könnte!")

# Erweiterung: mehrstufige Entscheidung
if weight > 30:
    print("Das ist auf jeden Fall ein Hund!")
elif weight > 8:
    print("Mittelgroßes Tier")
else:
    print("Eher ein kleines Tier")