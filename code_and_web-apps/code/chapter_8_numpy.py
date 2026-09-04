# Folge 8: Schneller rechnen mit NumPy
# Projekt: Unser XOR-Netz aus Folge 6, einmal mit Schleifen und einmal mit NumPy (nur versteckte Schicht),
# plus ein fairer Wettlauf zwischen beiden Varianten

import numpy as np
import time

# ---------- Variante 1: unser bekannter Ansatz mit Schleifen ----------

def neuron_schleife(eingaben, gewichte, schwellenwert):
    summe = 0
    for i in range(len(eingaben)):
        summe = summe + eingaben[i] * gewichte[i]
    return 1 if summe > schwellenwert else 0


def schicht_schleife(eingaben, alle_gewichte, alle_schwellenwerte):
    ausgaben = []
    for i in range(len(alle_gewichte)):
        ausgaben.append(neuron_schleife(eingaben, alle_gewichte[i], alle_schwellenwerte[i]))
    return ausgaben


# ---------- Variante 2: derselbe Gedanke, aber mit NumPy ----------
def schicht_numpy(eingaben, gewichte_matrix, schwellenwerte):
    # Eine einzige Matrixmultiplikation ersetzt die komplette doppelte Schleife
    summen = gewichte_matrix @ eingaben
    return (summen > schwellenwerte).astype(int)




# Gleiche Gewichte wie in Folge 6, nur jetzt als NumPy-Arrays organisiert
gewichte_versteckt = [
    [1.0, 1.0],    # ODER
    [-1.0, -1.0],  # NICHT-UND
]
schwellenwerte_versteckt = [0.5, -1.5]

gewichte_versteckt_np = np.array(gewichte_versteckt)
schwellenwerte_versteckt_np = np.array(schwellenwerte_versteckt)

eingabe = [1, 0]
eingabe_np = np.array(eingabe)


print("--- Vergleich: gleiches Ergebnis, zwei Wege ---")
ergebnis_schleife = schicht_schleife(eingabe, gewichte_versteckt, schwellenwerte_versteckt)
ergebnis_numpy = schicht_numpy(eingabe_np, gewichte_versteckt_np, schwellenwerte_versteckt_np)

print(f"Mit Schleifen : {ergebnis_schleife}")
print(f"Mit numpy: {ergebnis_numpy}")



# ---------- Der Wettlauf: viele Berechnungen, welcher Ansatz ist schneller? ----------

print("\n--- Geschwindigkeitstest ---")

anzahl_durchlaeufe = 1000000

start = time.time()
for _ in range(anzahl_durchlaeufe):
    schicht_schleife(eingabe, gewichte_versteckt, schwellenwerte_versteckt)
dauer_schleife = time.time() - start

start = time.time()
for _ in range(anzahl_durchlaeufe):
    schicht_numpy(eingabe_np, gewichte_versteckt_np, schwellenwerte_versteckt_np)
dauer_numpy = time.time() - start

print(f"{anzahl_durchlaeufe} Durchläufe mit Schleifen: {round(dauer_schleife, 4)} Sekunden")
print(f"{anzahl_durchlaeufe} Durchläufe mit NumPy: {round(dauer_numpy, 4)} Sekunden")
print(f"NumPy war ungefähr {round(dauer_schleife / dauer_numpy, 1)}-mal schneller!")

"""
    Warum sind wir langsamer mit numpy ?

    - Übergang von Python zu NumPy/kompiliertem Code
    - Matrixmultiplikation starten
    - temporäre NumPy-Arrays für summen und das Vergleichsergebnis erzeugen
    - Ergebnis wieder als Array bereitstellen
"""
