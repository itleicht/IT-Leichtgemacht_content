# Folge 7: Der Maschine das Lernen beibringen
# Projekt: Ein Neuron lernt selbstständig, ein UND-Gatter zu erkennen

def neuron(eingaben, gewichte, schwellenwert):
    summe = 0
    for i in range(len(eingaben)):
        summe = summe + eingaben[i] * gewichte[i]

    if summe > schwellenwert:
        return 1
    else:
        return 0


# Trainingsdaten: UND-Gatter
# Ausgabe soll nur 1 sein, wenn BEIDE Eingaben 1 sind
trainingsdaten = [
    ([0, 0], 0), # Zu den jeweiligen Eingaben [0,0] übergeben wir die Lösung als sogn. Label 
    ([0, 1], 0), # Der gesamte Datensatz aus Eingaben und Ausgabe ergibt die Trainingsdaten
    ([1, 0], 0),
    ([1, 1], 1),
]

# Wir starten mit schlechten, zufällig gewählten Gewichten
gewichte = [-0.5, 0.1]
schwellenwert = 0.5
lernrate = 0.2 # learning rate

print("--- Vor dem Training ---")
for eingaben, erwartet in trainingsdaten:
    vorhersage = neuron(eingaben, gewichte, schwellenwert)
    print(f"Eingabe {eingaben} - > Vorhersage: {vorhersage} (erwartet: {erwartet})")



# Die Lernregel: Nach jeder Vorhersage schauen wir, wie falsch wir lagen,
# und schieben die Gewichte ein kleines Stück in die richtige Richtung.
print("\n--- Training läuft ---")

anzahl_durchlaeufe = 10 # Epochen

for durchlauf in range(anzahl_durchlaeufe):
    for eingaben, erwartet in trainingsdaten:
        vorhersage = neuron(eingaben, gewichte, schwellenwert)
        fehler = erwartet - vorhersage # 0, wenn richtig, sonst +1 oder -1

        if fehler != 0:
            for i in range(len(gewichte)):
                gewichte[i] = gewichte[i] + lernrate * fehler * eingaben[i]
    print(f"Nach Durchlauf {durchlauf + 1}: Gewichte = {gewichte}")

print("\n--- Nach dem Training ---")
alle_richtig = True # Boolsche Variable
for eingaben, erwartet in trainingsdaten:
    vorhersage = neuron(eingaben, gewichte, schwellenwert)
    status = "richtig" if vorhersage == erwartet else "FALSCH"
    if vorhersage != erwartet:
        alle_richtig = False
    print(f"Eingabe {eingaben} -> Vorhersage: {vorhersage} ( erwartet: {erwartet})")

if alle_richtig: # heißt soviel wie if alle_richtig == True
    print("\n Das Neuron hat das UND-Gatter komplett selbst gelernt!")
