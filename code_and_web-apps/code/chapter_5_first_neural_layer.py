# Folge 5: Eine ganze Schicht aus Neuronen
# Projekt: Mehrere Neuronen zu einer Schicht verketten

def neuron(eingaben, gewichte, schwellenwert):
    summe = 0
    for i in range(len(eingaben)):
        summe = summe + eingaben[i] * gewichte[i]

    if summe > schwellenwert:
        return 1
    else:
        return 0

def schicht(eingaben, alle_gewichte, alle_schwellwerte):
    # Eine Schicht besteht aus mehreren Neuronen
    # Jedes Neuron bekommt dieselben Eingaben, aber eigene Gewichte und einen eigenen Schwellwert
    ausgaben = []
    for i in range(len(alle_gewichte)):
        ergebnis = neuron(eingaben, alle_gewichte[i], alle_schwellwerte[i])
        ausgaben.append(ergebnis)
    return ausgaben

# Beispiel: Soll ich heute joggen gehen, schwimmen gehen, oder zuhause bleiben?
# Eingaben: [Wetter gut (1/0), habe ich Zeit (1/0), habe ich Lust (1/0)]
eingaben = [1, 1, 0]

# Drei Neuronen in der Schicht, jedes mit eigenen Gewichten
gewichte_joggen = [0.3, 0.3, 0.6]
gewichte_schwimmen = [0.5, 0.2, 0.5]
gewichte_zuhause_bleiben = [-0.4, -0.2, 0.3]

alle_gewichte = [gewichte_joggen, gewichte_schwimmen, gewichte_zuhause_bleiben]
alle_schwellwerte = [0.5, 0.6, 0.1]

ergebnisse = schicht(eingaben, alle_gewichte, alle_schwellwerte)

aktivitaeten = ["Joggen", "Schwimmen", "Zuhause bleiben"]

print("Ergebnisse der Schicht:")
for i in range(len(ergebnisse)):
    if ergebnisse [i] == 1:
        status = "JA"
    else:
        status = "NEIN"
    print(aktivitaeten[i] + ": " + status)

# Bonus: Mehrere Situationen durchtesten
print("\n--- Weitere Tests ---")

test_situationen = [
    [1, 1, 1],  # perfekter Tag
    [0, 0, 0],  # schlechter Tag
    [1, 0, 0],  # gutes Wetter, aber keine Zeit und keine Lust
]

for situation in test_situationen:
    
    ergebnisse = schicht(situation, alle_gewichte, alle_schwellwerte)
    print("\nEingabe " + str(situation) + ":")
    for i in range(len(ergebnisse)):
        if ergebnisse[i] == 1:
            status = "JA"
        else:
            status = "NEIN"
        print(" " + aktivitaeten[i] + ": " + status)