################
# Aufgabe 4 a) #
################
print()
print("Aufgabe 4 a)")
print("============")

# AUFTRAG: Schreibe die Funktion `average`, welche den arithmetischen
# Durchschnitt für eine Liste von Zahlen berechnet.

def average(lst):
    # FIXME: Hier kommt dein Code
    ...

# Funktionierende Version:
# Falls du zu keiner Lösung kommst, kannst du die folgende Zeile
# ent-kommentieren, damit du weiter fahren kannst:

# from functions_lsg import average

# Tests: Assertions zum überprüfen, ob dein Code korrekt ist:
assert average([1, 2, 3]) == 2.0
assert average([7, 7, 7]) == 7.0
assert average([2, 3, 6, 7]) == 4.5
print("-*- Aufgabe 4 a) erledigt! -*-")

################
# Aufgabe 4 b) #
################
print()
print("Aufgabe 4 b)")
print("============")

# AUFTRAG: Implementiere die `fib`-Funktion, welche die n-te Zahl der
# Fibonacci-Folge berechnet.  Die Definition der Fibonacci-Folge findest
# du auf dem Aufgabenblatt.
#
# Wichtig: Die Funktion `fib` *muss* das Resultat *rekursiv* berechnen.

def fib(n):
    # FIXME: Hier kommt dein Code
    ...

# Funktionierende Version:
# from functions_lsg import fib

# Tests:
assert fib(0) == 0
assert fib(1) == 1
assert fib(5) == 5
assert fib(10) == 55
assert fib(15) == 610
print("-*- Aufgabe 4 b) erledigt! -*-")

################
# Aufgabe 4 c) #
################
print()
print("Aufgabe 4 c)")
print("============")

# AUFTRAG: Beobachte das Laufzeitverhalten der `fib`-Funktion mit dem
# unten zur Verfügung gestellten Code.  Passe den Range der Eingabewerte
# gegebenenfalls an.  Beantworte danach die unten gestellten Fragen in
# einem Codekommentar.

import time

for n in range(25, 30):
    start = time.perf_counter()
    fib(n)
    stop = time.perf_counter()
    print(f"fib({n}) took {stop - start:.2f} seconds")

# Frage i): Ab (zirka) welchem `n` benötigt `fib` mehr als eine Sekunde
# zur Berechnung des Resultats?
#
#
#
# Frage ii): Wie verhält sich die Laufzeit der `fib`-Funktion in
# Abhängigkeit des übergebenen Parameters `n`?  Sei möglichst präzis
# in deiner Beschreibung.
#
#
#
# Frage iii): Was sind die Gründe für das beobachtete Laufzeitverhalten?
#
#
#
print("-*- Aufgabe 4 c) erledigt? -*-")

################
# Aufgabe 4 d) #
################
print()
print("Aufgabe 4 d)")
print("============")

# AUFTRAG: Studiere den unten stehenden Code zur Decorator-Funktion
# `logger`.  Bearbeite danach den unten stehenden Auftrag.

# ==================================================================== #
# Die Logger-Funktion nimmt eine bestehende Funktion als Argument
# entgegen:
def logger(original_func):

    # Zuerst wird eine neue Funktion definiert:
    def new_func(arg):
        # Der Aufruf der Funktion wird auf der Konsole ausgegeben:
        print(f"Calling {original_func.__name__} with {arg!r}.")

        # Aus der neuen Funktion wird die ursprüngliche Funktion
        # aufgerufen, und ihr Rückgabewert unverändert zurück gegeben:
        return original_func(arg)

    # Zuletzt wird die neu kreierte Funktion zurück gegeben:
    return new_func

# Anwendung der logger-Funktion mit der decorator-Notation:
@logger
def foo(x):
    return x + 1


# Äquivalente Anwendung *ohne* decorator-Notation:
def bar(x):
    return x * 2

# bar mit der neu kreierten Funktion überschreiben:
bar = logger(bar)

foo(5)
bar("hu")
# ==================================================================== #

# AUFTRAG: Implementiere die beiden Decorator-Funktionen
# `result_incrementer` und `argument_incrementer`.
#
# `result_incrementer` soll den Aufruf an eine beliebige Funktion (mit
# einem einzigen Parameter) so verändern, dass das berechnete Resultat
# um eins erhöht wird.
#
# `argument_incrementer` soll den Aufruf an eine beliebige Funktion so
# verändern, dass der übergebene Parameter vor dem Aufruf der Funktion
# um eins erhöht wird.

def result_incrementer(original_func):
    def new_func(arg):
        # FIXME: Hier kommt dein Code:
        ...
    return new_func

def argument_incrementer(original_func):
    def new_func(arg):
        # FIXME: Hier kommt dein Code:
        ...
    return new_func

# Funktionierende Versionen:
# from functions_lsg import result_incrementer
# from functions_lsg import argument_incrementer

# Tests:
@result_incrementer
def f1(x):
    return x*x

@argument_incrementer
def f2(x):
    return x*x

assert f1(2) == 5
assert f1(3) == 10
assert f2(2) == 9
assert f2(3) == 16

print("-*- Aufgabe 4 d) erledigt! -*-")

################
# Aufgabe 4 e) #
################
print()
print("Aufgabe 4 e)")
print("============")

# AUFTRAG: In einem Cache-Zwischenspeicher sollen bereits berechnete
# Resultate zwischengespeichert werden.  `cache` ist also ein dict, in
# welchem unter den Eingabewerten die berechneten Resultate
# abgespeichert werden.
#
# Vervollständige den `cached`-Decorator, so dass
# - für Werte, welche bereits berechnet wurden, die Funktion nicht noch
#   einmal ausgeführt wird.  Vorhandene Resultate sollen direkt aus dem
#   Zwischenspeicher zurück gegeben werden.
# - falls die Funktion aufgerufen werden muss, das berechnete Resultat
#   im Zwischenspeicher abgespeichert wird, bevor das Resultat zurück
#   gegeben wird.

cache = {}
def cached(original_func):
    def new_func(x):
        # FIXME: Hier kommt dein Code:
        ...
    return new_func

# Funktionierende Version:
# from functions_lsg import cached

# Decorator anwenden:
fib = cached(fib)

# Tests: Ent-Kommentiere die folgenden Zeilen, um deinen Code zu testen:
# print(fib(100))
# assert fib(200) == 280571172992510140037611932413038677189525
# print("-*- Aufgabe 4 e) erledigt! Bravo! -*-")
