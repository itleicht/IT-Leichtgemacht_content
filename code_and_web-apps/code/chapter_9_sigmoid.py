# Folge 9: Das Netz verbessert sich selbst
# Projekt: Unser XOR-Netz aus Folge 6 lernt seine Gewichte komplett selbst,
# mit derselben Grundidee wie in Folge 7, nur jetzt für ein ganzes Netz mit zwei Schichten

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_ableitung(x):
    return x * (1 - x)


# Trainingsdaten: das XOR-Problem aus Folge 6
eingaben = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
])

erwartet = np.array([[0], [1], [1], [0]])

# Zufällig gewählte Startgewichte
np.random.seed(1)
gewichte_versteckt = np.random.uniform(-1, 1, (2, 2))
gewichte_ausgabe = np.random.uniform(-1, 1, (2, 1))
# print(gewichte_ausgabe)

# NEU: Bias, ein freier Zahlenwert pro Neuron, unabhängig von den Eingaben.
# Ohne Bias muss die Entscheidungsgrenze jedes Neurons zwingend durch den
# Nullpunkt gehen, das reicht bei XOR oft nicht aus, um sauber zu trennen.
bias_versteckt = np.random.uniform(-1, 1, (1, 2))
bias_ausgabe = np.random.uniform(-1, 1, (1, 1))
# print(bias_ausgabe)

lernrate = 0.5
anzahl_durchlaeufe = 10000

print("--- Vor dem Training ---")
versteckte_schicht = sigmoid(eingaben @ gewichte_versteckt + bias_versteckt)
ausgabe = sigmoid(versteckte_schicht @ gewichte_ausgabe + bias_ausgabe)
print(np.round(ausgabe, 3).flatten())


print("\n--- Training läuft ---")
for durchlauf in range(anzahl_durchlaeufe):


    # Vorwärtsrichtung: jetzt mit Bias in beiden Schichten
    versteckte_schicht = sigmoid(eingaben @ gewichte_versteckt + bias_versteckt)
    ausgabe = sigmoid(versteckte_schicht @ gewichte_ausgabe + bias_ausgabe)

    fehler_ausgabe = erwartet - ausgabe
    
    # Rückwärtsrichtung: den Fehler von der Ausgabe zurück zur versteckten Schicht schieben
    korrektur_ausgabe = fehler_ausgabe * sigmoid_ableitung(ausgabe)
    # print(korrektur_ausgabe)
    fehler_versteckt = korrektur_ausgabe @ gewichte_ausgabe.T
    korrektur_versteckt = fehler_versteckt * sigmoid_ableitung(versteckte_schicht)

    # Gewichte UND Bias anpassen. Der Bias bekommt die Summe der Korrektur
    # über alle vier Trainingsbeispiele, da er nicht von einer bestimmten Eingabe abhängt.
    gewichte_ausgabe += versteckte_schicht.T @ korrektur_ausgabe * lernrate
    bias_ausgabe += np.sum(korrektur_ausgabe, axis=0, keepdims=True) * lernrate
    gewichte_versteckt += eingaben.T @ korrektur_versteckt * lernrate
    bias_versteckt += np.sum(korrektur_versteckt, axis=0, keepdims=True) * lernrate

    if durchlauf % 2000 == 0:
        durchschnittlicher_fehler = np.mean(np.abs(fehler_ausgabe))
        print(f"Durchlauf {durchlauf}: durchschnittlicher Fehler = {round(durchschnittlicher_fehler, 4)}")


print("\n--- Nach dem Training ---")
versteckte_schicht = sigmoid(eingaben @ gewichte_versteckt + bias_versteckt)
ausgabe = sigmoid(versteckte_schicht @ gewichte_ausgabe + bias_ausgabe)
# print(ausgabe)

for i in range(len(eingaben)):
    gerundet = 1 if ausgabe[i][0] > 0.5 else 0
    print(f"Eingabe: {eingaben[i].tolist()} -> {round(ausgabe[i][0], 3)} -> gerundet: {gerundet} (Erwartet: {erwartet[i][0]})")
    