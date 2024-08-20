# Auftrag Grosi

Was immer du deinem Grosi sagst (besser gesagt tippst), ihre Antwort ist immer:

> WAAS?! RED LAUTER, ICH VERSTEH DICH NICHT MEIN SCHATZ!

Ausser natürlich du schreist sie an (schreibst alles in Grossbuchstaben). In diesem Fall antwortet sie mit:

> ACH NEIN, SEIT MINDESTENS DEN 60ERN DOCH NICHT MEHR!

Du kannst das Gespräch (Programm) beenden, indem du dem Grosi **TSCHÜSS** zu rufst.

Schreibe das Programm in eine Datei mit dem Namen `grosi.py`.

_Tipp 1:_ Um das Programm glaubwürdiger zu machen, sollte die Grossmutter mit verschiedenen Jahrzehnten antworten. Also 40ern, 50ern, usw.

Vielleicht hilft dir der folgenden Python-Code dabei:
```python
import random

zufallszahl = random.randrange(1, 10)
print(zufallszahl)
```

_Tipp 2:_ Überlege dir, welche Teile des Programms immer und immer wieder passieren. All diese Teile sollten innerhalb des `while`-Loops sein.

## Erweiterung

Kopiere die Datei `grosi.py` nach `grosi_extended.py`.

Was, wenn das Grosi nicht möchte, dass du weg gehst? Und wenn du TSCHÜSS rufst, tut sie einfach so, als hätte sie nichts gehört. Erweitere dein Programm so, dass du mindestens drei mal _hintereinander_ TSCHÜSS rufen musst. Teste ein Programm: Wenn du drei mal TSCHÜSS gesagt hast, jedoch nicht direkt hintereinander, solltest du immer noch im Gespräch mit deinem Grosi sein.
