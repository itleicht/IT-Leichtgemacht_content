# Folge 3: Der Text-Analyzer
# Projekt: Häufigste Wörter in einem Text finden (Bag of Words - Grundprinzip)

text = input("Gib mir einen Satz oder kurzen Text: ")

# Text in Kleinbuchstaben und in einzelne Wörter zerlegen
text_small = text.lower()
words = text_small.split()

# Ein leeres Wörterbuch, um zu zählen, wie oft jedes Wort vorkommt
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("Wort-Häufigkeiten:")
for word in frequency:
    print(word + ": " + str(frequency[word]))


# Das häufigste Wort finden
most_frequent_word = ""
highest_occurence = 0

for word in frequency:
    if frequency[word] > highest_occurence:
        highest_occurence = frequency[word]
        most_frequent_word = word

print("Das häufigste Wort ist " + most_frequent_word + " mit " + str(highest_occurence) + " Vorkommen.")

# Bonus: Nur Wörter ausgeben, die länger als 3 Zeichen sind
print("Lange Wörter mit mehr als 3 Buchstaben: ")
for word in words:
    if len(word) > 3:
        print(word)