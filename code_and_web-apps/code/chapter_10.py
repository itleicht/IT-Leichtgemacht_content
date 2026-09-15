# Folge 10: Ein neuer Algorithmus, ein neues Werkzeug
# Projekt: k-nächste-Nachbarn (kNN), unser erster Algorithmus ohne neuronales Netz,
# und der erste Kontakt mit Pandas

import pandas as pd
import math

# Ein winziger Datensatz: Größe und Gewicht ein paar bekannter Tiere
daten = pd.DataFrame({
    "groesse_cm": [25, 30, 45, 90, 95, 100, 20, 28],
    "gewicht_kg": [4, 5, 8, 30, 35, 32, 3, 4.5],
    "tier":       ["Katze", "Katze", "Katze", "Hund", "Hund", "Hund", "Katze", "Katze"]
})

print("--- Unser Datensatz ---")
print(daten)

def abstand(punkt1, punkt2):
    return math.sqrt((punkt1[0] - punkt2[0])**2 + (punkt1[1] - punkt2[1])**2)

def knn_vorhersage(neuer_punkt, daten, k):
    abstaende = []

    for index, zeile in daten.iterrows():
        bekannter_punkt = (zeile["groesse_cm"], zeile["gewicht_kg"])
        d = abstand(neuer_punkt, bekannter_punkt)
        abstaende.append((d, zeile["tier"]))

    abstaende.sort(key=lambda x: x[0])
    naechste_nachbarn = abstaende[:k]

    print(f"\nDie {k} nächsten Nachbarn zu {neuer_punkt} :")
    for d, tier in naechste_nachbarn:
        print(f"{tier} (Abstand: {round(d, 2)})")

    stimmen = {}

    for d, tier in naechste_nachbarn:
        if tier in stimmen:
            stimmen[tier] = stimmen[tier] + 1
        else:
            stimmen[tier] = 1

    gewinner = max(stimmen, key=stimmen.get)

    return gewinner


# Ein neues, unbekanntes Tier: 40 cm groß, 7 kg schwer
neues_tier = (40, 7)
k = 3

vorhersage = knn_vorhersage(neues_tier, daten, k)
print(f"\nVorhersage für {neues_tier}: {vorhersage}")


# Bonus: mehrere unbekannte Tiere durchtesten
print("\n--- Weitere Tests ---")
testfaelle = [(80, 28), (22, 3.5), (60, 15)]

for tier in testfaelle:
    ergebnis = knn_vorhersage(tier, daten, k)
    print(f"Eingabe {tier} -> Vorhersage: {ergebnis}")

