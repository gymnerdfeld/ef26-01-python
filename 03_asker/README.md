# Auftrag Fragesteller

In einem ersten Schritt erstellen wir einen Datei `asker.py` welche die Person nach ihrem Alter fragt, und ihr zurück gibt, wie alt sie nächstes Jahr wird.

So könnte die Ausgabe des Programmes lauten:

> Wie alt bist du? **19**
> Dann wirst du nächstes Jahr 20.

Falls die Person keine Zahl eingibt, wird die Frage wiederholt:

> Wie alt bist du? **neunzehn**
> Ungültige Eingabe, versuch es noch einmal.
> Wie alt bist du? ...

### Zusatzaufgabe

Kreiere nun mit dem oben erstellten Code eine Funktion `input_int`, welche die Frage so lange wiederholt, bis der:ie Benutzer:in eine korrekte Zahl eingegeben hat.

Die Funktion sollte folgendermassen benutzt werden können:
```py
age = input_int("Wie alt bist du? ")
print(f"Dann wirst du nächstes Jahr {age + 1}")
```

### Zusatzaufgabe 2 (freiwillig)

Kreiere deine eigene Funktion `isdecimal` mit dem gleichen Verhalten von Pythons `isdecimal` für Strings.

### Zusatzaufgabe 3

Kreiere eine Funktion `input_choice`, welche die Frage und eine Liste mit gültigen Antworten entgegen nimmt.