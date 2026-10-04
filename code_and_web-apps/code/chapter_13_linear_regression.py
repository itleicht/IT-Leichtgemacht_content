"""
Folge 13: Lineare Regression

Der erste Algorithmus der Serie, der keine Klasse vorhersagt (ja/nein,
Katze/Hund), sondern eine Zahl. Wir suchen die Gerade
    Miete = steigung * Wohnflaeche + achsenabschnitt
die am besten zu den Trainingsdaten passt - mit demselben Werkzeug,
das wir schon von den neuronalen Netzen kennen: Gradientenabstieg.
"""

import pandas as pd


def vorhersage(x, steigung, achsenabschnitt):
    """Wert auf der aktuellen Geraden an der Stelle x."""
    return steigung * x + achsenabschnitt


def fehler(daten, steigung, achsenabschnitt, x_spalte, y_spalte):
    """Mittlerer quadratischer Fehler (MSE) über alle Trainingsdaten."""
    fehler_summe = 0
    for _, zeile in daten.iterrows():
        vorhergesagt = vorhersage(zeile[x_spalte], steigung, achsenabschnitt)
        fehler_summe += (vorhergesagt - zeile[y_spalte])
    return fehler_summe / len(daten)



def gradienten_berechnen(daten, steigung, achsenabschnitt, x_spalte, y_spalte):
    """Wie stark und in welche Richtung sich Steigung und Achsenabschnitt
    ändern müssen, um den Fehler zu verkleinern."""
    n = len(daten)
    steigung_gradient = 0
    achsenabschnitt_gradient = 0

    for _, zeile in daten.iterrows():
        x = zeile[x_spalte]
        y = zeile[y_spalte]
        vorhergesagt = vorhersage(x, steigung, achsenabschnitt)
        differenz = vorhergesagt - y

        steigung_gradient += 2 * differenz * x
        achsenabschnitt_gradient += 2 * differenz

    return steigung_gradient / n, achsenabschnitt_gradient / n


def trainieren(daten, x_spalte, y_spalte, lernrate=0.0001, epochen=1000):
    """Passt Steigung und Achsenabschnitt schrittweise per
    Gradientenabstieg an die Trainingsdaten an."""
    steigung = 0.0
    achsenabschnitt = 0.0

    for epoche in range(epochen):
        steigung_gradient, achsenabschnitt_gradient = gradienten_berechnen(daten, steigung, achsenabschnitt, x_spalte, y_spalte)
        steigung -= lernrate * steigung_gradient
        achsenabschnitt -= lernrate * achsenabschnitt_gradient

        if epoche % 200 == 0:
            aktueller_fehler = fehler(daten, steigung, achsenabschnitt, x_spalte, y_spalte)
            print(f"Epoche {epoche}: Fehler = {aktueller_fehler:.2f}, "
                  f"Steigung = {steigung:.4f}, Achsenabschnitt = {achsenabschnitt:.4f}")
            
    return steigung, achsenabschnitt

    


if __name__ == "__main__":

    wohnungsdaten = pd.DataFrame({
        "Wohnflaeche": [35, 42, 50, 55, 61, 68, 72, 80, 88, 95, 102, 110],
        "Miete":       [420, 480, 560, 610, 670, 730, 790, 860, 930, 1000, 1080, 1150],
    })
    
    print("=== Training startet ===")
    steigung, achsenabschnitt = trainieren(
        wohnungsdaten, "Wohnflaeche", "Miete", lernrate=0.00005, epochen=2000
    )

    print(f"\nGelernte Gerade: Miete = {steigung:.2f} * Wohnfläche + {achsenabschnitt:.2f}")

    # Bonus: Vorhersagen für neue Wohnungen
    neue_flaechen = [45, 75, 120]
    print("\n=== Vorhersagen für neue Wohnungen ===")
    for flaeche in neue_flaechen:
        geschaetzte_miete = vorhersage(flaeche, steigung, achsenabschnitt)
        print(f"{flaeche} qm -> geschaetzte Miete: {geschaetzte_miete:.2f} €")
