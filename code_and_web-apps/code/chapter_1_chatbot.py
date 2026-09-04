# Folge 1: Der erste Handshake mit der Maschine
# Schritt 1: Ausgabe
print("Hallo, ich bin dein erster Chatbot!")

# Schritt 2: Eingabe vom Nutzer
name = input("Wie heißt du? ") # Eingabe des Users ist immer ein String


# Schritt 3: Beides verbinden - das Programm reagiert auf die Eingabe
print("Schön, dich kennenzulernen, " + name + "!") # String - Konkatenation

# Schritt 4: Alter eingeben
age = input("Wie alt bist du? ")

# Schritt 5: Mit dem Alter rechnen
print("Du bist " + age + " Jahre alt")
age = int(age)

# Schritt 6: Übungslösung (Jahr berechnen, in dem man 100 wird)
year_now = 2026
year_100 = year_now + (100 - age)
print(name + ", im Jahr " + str(year_100) + " wirst du 100 Jahre alt!")
