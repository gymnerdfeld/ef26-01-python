# Auftrag Rekursion

## Fakultät

Schreibe in der Datei `fakultaet.py` die Funktion `fact` welche die Fakultät einer natürlichen Zahl berechnet.

Die Fakultät ist folgendermassen definiert:
$0! = 1$
$1! = 1$
$2! = 2$
$n! = 1\cdot2\cdot\ldots\cdot n$

### Rekursive Definition

Die Fakultät kann auch rekursiv (auf sich selbst beziehend) definiert werden:

$0! = 1$
$n! = n\cdot (n-1)!$

Versuche, diese rekursive Definition als Vorbild für deine Funktionsdefinition zu nehmen.

## Palindrom

Schreibe in der Datei `palindrome.py` die Funktion `ispalindrome`, welche überprüft, ob ein eingegebenes Wort ein Palindrom ist.

```
>>> ispalindrome("anna")
True
>>> ispalindrome("hans")
False
>>> ispalindrome("wasitacatisaw")
True
```

### Rekursive Definition

Versuche die Funktion `ispalindrome` Rekursiv zu definieren. Überlege dir dazu zuerst, welches die trivialen Fälle sind, bei welchen ohne den Inhalt des Wortes anzuschauen mit Sicherheit sagen können, dass es sich um ein Palindrom handeln muss. Überlege als zweites wie du von einem beliebigen Wort zum trivialen Fall gelangen könntest.

_Tipp:_ In Python kann man Teile aus einen Wort "ausschneiden":

```
>>> wort = "Kuchenstück"
>>> wort[3:8]
'henst'
wort[2:-4]
'chens'
```
