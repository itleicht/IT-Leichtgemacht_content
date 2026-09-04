# Folge 4: Das erste künstliche Neuron
# Projekt: Ein einzelnes Neuron in purem Python nachbauen

def neuron(eingaben, gewichte, schwellwert):
    # Schritt 1: Jede Eingabe mit ihrem Gewicht multiplizieren und aufsummieren
    summe = 0
    for i in range(len(eingaben)):
        summe = summe + eingaben[i] * gewichte[i]

    # Schritt 2: Entscheidung treffen - feuert das Neuron oder nicht ?
    if summe > schwellwert:
        return 1 # Neuron "Feuert"
    else:
        return 0 # Neuron bleibt still


# Beispiel: Soll ich heute joggen gehen?
# Eingaben: [Wetter gut (1) oder schlecht (0), habe ich Zeit (1) oder nicht (0), habe ich Lust (1) oder nicht (0)]
eingaben = [1,1,0]

# Gewichte: wie wichtig ist jede Eingabe? (hier: Lust zählt am meisten)
gewichte = [0.3, 0.3, 0.6]

schwellwert = 0.5

ergebnis = neuron(eingaben, gewichte, schwellwert)

if ergebnis == 1:
    print("Das Neuron feuert: Geh bitte joggen!")
else:
    print("Das Neuron feuert nicht: Heute lieber nicht.")

print("Berechnete Summe war ausschlaggebend für das Ergebnis.")

# Bonus: Mehrere Beispiele durchtesten
print("\n--- Weitere Tests ---")

test_faelle = [
    [1,1,1], # alles positiv
    [0,0,0], # nichts positiv
    [1,0,1]
]

for fall in test_faelle:
    ergebnis = neuron(fall, gewichte, schwellwert)
    print("Eingabe " + str(fall) + " -> Ergebnis: " + str(ergebnis))