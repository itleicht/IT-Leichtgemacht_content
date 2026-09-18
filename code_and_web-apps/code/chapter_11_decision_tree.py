"""
Folge 11: "Eine Maschine, die Fragen stellt"
Ein Entscheidungsbaum von Hand - ohne fertige Bibliothek, ohne Formeln.

Idee: Statt Informationsgewinn/Entropie mit einer Formel zu berechnen,
zählen wir einfach: Wenn wir nach einer bestimmten Spalte aufteilen und
in jeder entstandenen Gruppe die Mehrheitsklasse raten - wie viele Fälle
liegen wir dann richtig? Die Spalte mit den meisten richtigen
Vorhersagen wird als nächste Frage im Baum ausgewählt.
"""

import pandas as pd


def bewertung_der_frage(daten, spalte, ziel_spalte):
    """
    Bewertet, wie gut eine Spalte als nächste Frage geeignet ist.
    Wir teilen die Daten nach jedem Wert der Spalte auf, raten pro
    Gruppe die Mehrheitsklasse und zählen die Treffer zusammen.
    """
    richtige_vorhersagen = 0
    for wert in daten[spalte].unique(): # Anzahl der vokommenden Merkmalsausprägungen
        gruppe = daten[daten[spalte] == wert] # Die Daten jeder Gruppe in gruppe speichern
        merheitsklasse = gruppe[ziel_spalte].value_counts().idxmax() # Die Mehrheitsklasse der Gruppe bestimmen
        richtige_vorhersagen += (gruppe[ziel_spalte] == merheitsklasse).sum() # Die Anzahl der richtigen Vorhersagen in dieser Gruppe zählen und der Gesamtzahl hinzufügen

    return richtige_vorhersagen

def beste_frage(daten, verfuegbare_spalten, ziel_spalte):
    """Sucht unter den verfügbaren Spalten diejenige mit der besten Bewertung."""
    beste_spalte = None
    beste_bewertung = -1
    for spalte in verfuegbare_spalten:
        bewertung = bewertung_der_frage(daten, spalte, ziel_spalte)
        if bewertung > beste_bewertung:
            beste_bewertung = bewertung
            beste_spalte = spalte
    return beste_spalte


def baum_bauen(daten, verfuegbare_spalten, ziel_spalte, tiefe=0):
    """
    Baut rekursiv einen Entscheidungsbaum aus verschachtelten Wenn-Dann-Fragen.

    Ein Blatt ist einfach ein String (die vorhergesagte Klasse, z.B. "ja").
    Ein innerer Knoten ist ein Dictionary:
        {"frage": spaltenname, "aeste": {wert1: unterbaum1, wert2: unterbaum2, ...}}
    """
    zielwerte = daten[ziel_spalte]

    # Abbruch 1: Alle übrig gebliebenen Fälle gehören zur gleichen Klasse
    if zielwerte.nunique() == 1:
        return zielwerte.iloc[0]

    # Abbruch 2: Keine Spalten mehr übrig -> Mehrheitsklasse als Blatt nehmen
    if len(verfuegbare_spalten) == 0:
        return zielwerte.value_counts().idxmax()
    
    # Beste Spalte für die nächste Frage auswählen
    spalte = beste_frage(daten, verfuegbare_spalten, ziel_spalte)
    einrueckung = " " * tiefe
    print(f"{einrueckung}Frage: Wie ist {spalte}?")

    uebrige_spalten = [s for s in verfuegbare_spalten if s != spalte]
    aeste = {}

    for wert in daten[spalte].unique():
        teilmenge = daten[daten[spalte] == wert]
        print(f"{einrueckung} -> {wert}")
        aeste[wert] = baum_bauen(teilmenge, uebrige_spalten, ziel_spalte, tiefe +2)

    return {"frage": spalte, "aeste": aeste}


def vorhersage(baum, fall):
    """
    Läuft einen neuen Fall (Dictionary mit Merkmalen) durch den Baum,
    bis ein Blatt - also eine Klasse - erreicht ist.
    """
    # Blatt erreicht: baum ist einfach ein String wie "ja" oder "nein"
    if not isinstance(baum, dict):
        return baum
    
    spalte = baum["frage"]
    wert_im_fall = fall[spalte]

    # Falls der Wert im Trainingsbaum nie vorkam, raten wir sicherheitshalber "nein"
    if wert_im_fall not in baum["aeste"]:
        return "nein"

    naechster_teilbaum = baum["aeste"][wert_im_fall]
    return vorhersage(naechster_teilbaum, fall)


if __name__ == "__main__":
    # Datensatz als Pandas DataFrame (Werkzeug aus Folge 10)
    daten = pd.DataFrame({
        "Wetter":          ["Sonnig", "Sonnig", "Bewölkt", "Regen", "Regen", "Regen", "Bewölkt",
                             "Sonnig", "Sonnig", "Regen", "Sonnig", "Bewölkt", "Bewölkt", "Regen"],
        "Temperatur":      ["Warm", "Warm", "Warm", "Mild", "Kühl", "Kühl", "Kühl",
                             "Mild", "Kühl", "Mild", "Mild", "Mild", "Warm", "Mild"],
        "Luftfeuchtigkeit": ["Hoch", "Hoch", "Hoch", "Hoch", "Normal", "Normal", "Normal",
                             "Hoch", "Normal", "Normal", "Normal", "Hoch", "Normal", "Hoch"],
        "Wind":            ["Schwach", "Stark", "Schwach", "Schwach", "Schwach", "Stark", "Stark",
                             "Schwach", "Schwach", "Schwach", "Stark", "Stark", "Schwach", "Stark"],
        "Spielen":         ["nein", "nein", "ja", "ja", "ja", "nein", "ja",
                             "nein", "ja", "ja", "ja", "ja", "ja", "nein"],
    })
    # print(daten)

    zielspalte = "Spielen"

    # merkmalsspalten = []
    # for spalte in daten.columns():
    #     if spalte != zielspalte:
    #         merkmalsspalten.append(spalte)
            
    merkmalsspalten = [spalte for spalte in daten.columns if spalte != zielspalte]

    print("=== Wir bauen den Entscheidungsbaum ===")
    baum = baum_bauen(daten, merkmalsspalten, zielspalte)

    print("\n=== Fertiger Baum (als verschachteltes Dictionary) ===")
    print(baum)

    unser_Testfall = {"Wetter": "Sonnig", "Temperatur": "Kühl", "Luftfeuchtigkeit": "Normal", "Wind": "Schwach"}
    ergebnis = vorhersage(baum, unser_Testfall)
    print("\n=== Testfall ===")
    print(f"{unser_Testfall} -> Spielen: {ergebnis}")



    # Bonus: mehrere Testfälle durch den fertigen Baum schicken
    testfaelle = [
        {"Wetter": "Sonnig", "Temperatur": "Kühl", "Luftfeuchtigkeit": "Normal", "Wind": "Schwach"},
        {"Wetter": "Regen", "Temperatur": "Mild", "Luftfeuchtigkeit": "Hoch", "Wind": "Stark"},
        {"Wetter": "Bewölkt", "Temperatur": "Warm", "Luftfeuchtigkeit": "Normal", "Wind": "Stark"},
    ]

    print("\n=== Testfälle ===")
    for fall in testfaelle:
        ergebnis = vorhersage(baum, fall)
        print(f"{fall} -> Spielen: {ergebnis}")
    