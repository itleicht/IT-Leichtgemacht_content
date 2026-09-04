# Folge 6: Warum ein Neuron nicht reicht
# Projekt: Das XOR-Problem, und wie eine zweite Schicht es löst

def neuron(eingaben, gewichte, schwellenwert):
    summe = 0
    for i in range(len(eingaben)):
        summe = summe + eingaben[i] * gewichte[i]

    if summe > schwellenwert:
        return 1
    else:
        return 0


# XOR: Die Ausgabe soll 1 sein, wenn GENAU EINE der beiden Eingaben 1 ist,
# aber nicht beide gleichzeitig.
xor_faelle = [
    [0, 0],  # soll 0 ergeben
    [0, 1],  # soll 1 ergeben
    [1, 0],  # soll 1 ergeben
    [1, 1],  # soll 0 ergeben
]

print("--- Versuch 1: Ein einzelnes Neuron ---")

# Wir probieren ein paar Gewichte aus - egal welche, es klappt nicht für alle vier Fälle
gewichte_versuch = [0.1, 1.0]
schwellwert_versuch = 1.0

for fall in xor_faelle:
    ergebnis = neuron(fall, gewichte_versuch, schwellwert_versuch)
    print("Eingabe " + str(fall) + " -> Ergebnis: " + str(ergebnis))



# Versuch 2:

print("\n--- Versuch 2: Zwei Schichten hintereinander ---")

def schicht(eingaben, alle_gewichte, alle_schwellenwerte):
    ausgaben = []
    for i in range(len(alle_gewichte)):
        ergebnis = neuron(eingaben, alle_gewichte[i], alle_schwellenwerte[i])
        ausgaben.append(ergebnis)
    return ausgaben


# Versteckte Schicht: zwei Neuronen, die zwei einfachere Teilaufgaben lösen
# Neuron A: "mindestens eine Eingabe ist 1" (ODER)
# Neuron B: "nicht beide Eingaben sind 1" (NICHT-UND)
gewichte_versteckt = [
    [1.0, 1.0], # Neuron A: ODER
    [-1.0, -1.0] # Neuron B: NICHT-UND
]
schwellwerte_versteckt = [0.5, -1.5]

# Ausgabeschicht: ein Neuron, das beide Teilergebnisse kombiniert (UND)
gewichte_ausgabe = [[1.0, 1.0]]
schwellwert_ausgabe = [1.5]

for fall in xor_faelle:
    versteckte_ausgabe = schicht(fall, gewichte_versteckt, schwellwerte_versteckt)
    finale_ausgabe = schicht(versteckte_ausgabe, gewichte_ausgabe, schwellwert_ausgabe)
    print("Eingabe " + str(fall) + " -> verstecktes Ergebnis: " + str(versteckte_ausgabe) + " -> finale Ausgabe: " + str(finale_ausgabe[0]))

print("\n Mit einer zweiten Schicht klappt XOR einwandfrei!")

