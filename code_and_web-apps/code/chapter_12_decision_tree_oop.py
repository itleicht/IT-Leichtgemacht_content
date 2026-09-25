"""
Folge 12: "Ordnung ins Chaos bringen (OOP)"

Der Entscheidungsbaum aus Folge 11 bekommt eine eigene Klasse.
Die Berechnungen selbst bleiben unverändert - nur das, was vorher bei
jedem Aufruf als Parameter mitgeschleppt wurde (Zielspalte, Baum),
steckt jetzt in der Instanz.

Methoden, die nur intern für den Baumbau gebraucht werden, tragen
einen führenden Unterstrich (_bewertung_der_frage, _beste_frage,
_baum_bauen). Von außen wird nur die Instanz erzeugt und
anschließend vorhersage(fall) aufgerufen.
"""

import pandas as pd

class Entscheidungsbaum:

    def __init__(self, daten, verfuegbare_spalten, ziel_spalte):
        self.ziel_spalte = ziel_spalte
        self.baum = self._baum_bauen(daten, verfuegbare_spalten)

    def _bewertung_der_frage(self, daten, spalte):
        """
        Bewertet, wie gut eine Spalte als nächste Frage geeignet ist.
        Wir teilen die Daten nach jedem Wert der Spalte auf, raten pro
        Gruppe die Mehrheitsklasse und zählen die Treffer zusammen.
        """
        richtige_vorhersagen = 0
        for wert in daten[spalte].unique(): # Anzahl der vokommenden Merkmalsausprägungen
            gruppe = daten[daten[spalte] == wert] # Die Daten jeder Gruppe in gruppe speichern
            merheitsklasse = gruppe[self.ziel_spalte].value_counts().idxmax() # Die Mehrheitsklasse der Gruppe bestimmen
            richtige_vorhersagen += (gruppe[self.ziel_spalte] == merheitsklasse).sum() # Die Anzahl der richtigen Vorhersagen in dieser Gruppe zählen und der Gesamtzahl hinzufügen

        return richtige_vorhersagen

    def _beste_frage(self, daten, verfuegbare_spalten):
        """Sucht unter den verfügbaren Spalten diejenige mit der besten Bewertung."""
        beste_spalte = None
        beste_bewertung = -1
        for spalte in verfuegbare_spalten:
            bewertung = self._bewertung_der_frage(daten, spalte)
            if bewertung > beste_bewertung:
                beste_bewertung = bewertung
                beste_spalte = spalte
        return beste_spalte

    def _baum_bauen(self, daten, verfuegbare_spalten):
        """
        Baut rekursiv einen Entscheidungsbaum aus verschachtelten Wenn-Dann-Fragen.

        Ein Blatt ist einfach ein String (die vorhergesagte Klasse, z.B. "ja").
        Ein innerer Knoten ist ein Dictionary:
            {"frage": spaltenname, "aeste": {wert1: unterbaum1, wert2: unterbaum2, ...}}
        """
        zielwerte = daten[self.ziel_spalte]

        # Abbruch 1: Alle übrig gebliebenen Fälle gehören zur gleichen Klasse
        if zielwerte.nunique() == 1:
            return zielwerte.iloc[0]

        # Abbruch 2: Keine Spalten mehr übrig -> Mehrheitsklasse als Blatt nehmen
        if len(verfuegbare_spalten) == 0:
            return zielwerte.value_counts().idxmax()
        
        # Beste Spalte für die nächste Frage auswählen
        spalte = self._beste_frage(daten, verfuegbare_spalten)
        uebrige_spalten = [s for s in verfuegbare_spalten if s != spalte]
        aeste = {}

        for wert in daten[spalte].unique():
            teilmenge = daten[daten[spalte] == wert]
            aeste[wert] = self._baum_bauen(teilmenge, uebrige_spalten)

        return {"frage": spalte, "aeste": aeste}

    def vorhersage(self, fall):
        """
        Läuft einen neuen Fall (Dictionary mit Merkmalen) durch den Baum,
        bis ein Blatt - also eine Klasse - erreicht ist.
        """
        aktueller_teilbaum = self.baum

        while isinstance(aktueller_teilbaum, dict):
            spalte = aktueller_teilbaum["frage"]
            wert_im_fall = fall[spalte]

            if wert_im_fall not in aktueller_teilbaum["aeste"]:
                return "nein"

            aktueller_teilbaum = aktueller_teilbaum["aeste"][wert_im_fall]

        return aktueller_teilbaum

if __name__ == "__main__":

    wetterdaten = pd.DataFrame({
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

    merkmalsspalten = [spalte for spalte in wetterdaten.columns if spalte != "Spielen"]

    baum_objekt = Entscheidungsbaum(wetterdaten, merkmalsspalten, ziel_spalte="Spielen")

    testfall = {"Wetter": "Regen", "Temperatur": "Mild", "Luftfeuchtigkeit": "Hoch", "Wind": "Schwach"}
    print(f"Testfall {testfall} -> Spielen: {baum_objekt.vorhersage(testfall)}")


