# Hangman

Schreibe in der Datei `hangman.py` das Spiel Hangman.

Spiele bevor du startest eine Runde Hangman auf Papier mit jemanden aus der Klasse.

In einer ersten Version soll das Programm nur die richtig geratenen Buchstaben, und die noch nicht erratenen Leerstellen anzeigen:

```
_ A _ _ _ S _ _ A
```

Das zu erratende Wort ist fest in den Code einprogrammiert, und der:ie Benutzer:in soll beliebig oft raten können.

## Erweiterungen

### Anzahl Versuche

Limitiere die Anzahl Versuche auf ein sinnvolle Zahl. Wird diese Anzahl überschritten, ist das Spiel zu Ende.

### Bereits benutzte Buchstaben

Verhindere, dass bereits benutze Buchstaben noch einmal eingegeben werden können. Zeige als Hilfestellung die Liste der Buchstaben der Fehlversuche dar.

### Grafische Darstellung

Stelle die Anzahl Fehlversuche grafisch dar. Zum Beispiel so:

```
  --------
  | /
  |/
  |
  |
  |
/---\
```

_Tipp:_ Verwenden den Befehl `os.system("cls")`um den Bildschirm zu löschen, und starte das Programm in der Windows Konsole (Tastenkombination `Ctrl+T` oder im Menu `Run` Eintrag `Run current script in terminal` auswählen).

### Zufälliges Wort wählen

Das zu erratende Wort soll zufällig aus einer grossen Liste von Wörtern ausgewählt werden. Verwende dazu die Funktion `choice` aus der Bibliothek `random`:

```py
>>> import random
>>> words = ["kuh", "hahn", "ziege"]
>>> random.choice(words)
'ziege'
```

_Tipp:_ Speichere die Liste der Wörter in einer separaten Datei, und lies diese bei Programmstart ein.
