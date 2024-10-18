import random, os

words = []
with open("words.txt") as f:
    for line in f:
        line = line.strip()
        if line != "":
            words.append(line.upper())

word = random.choice(words).upper()

done = False
wordset = set(word)
misses = []
hits = set()


def print_hangman():
    a = "|" if len(misses) > 0 else " "
    b = "-" if len(misses) > 1 else " "
    c = "/" if len(misses) > 2 else " "
    d = "|" if len(misses) > 3 else " "
    e = "O" if len(misses) > 4 else " "
    f1 = "\\" if len(misses) > 5 else " "
    f2 = "/" if len(misses) > 5 else " "
    f3 = "|" if len(misses) > 5 else " "

    w = word
    for letter in word:
        if letter not in hits:
            w = w.replace(letter, "_")

    used = ", ".join(misses)

    os.system("cls")
    print(
        f"""\
  {b * 8}
  {a} {c}    {d}
  {a}{c}    {f1}{e}{f2}
  {a}      {f3}          {w}
  {a}     {f2} {f1}
  {a}                 Schon verwendet: {used}
/---\\\
"""
    )


def read_letter():
    done = False
    while not done:
        c = input("Wähle einen Buchstaben: ").strip().upper()
        if len(c) > 1:
            print("Bitte nur einen Buchstaben auf's Mal eingeben")
        elif len(c) == 0:
            print("Bitte einen Buchstaben eingeben")
        elif c not in "ABCDEFGHIJKLMNOPQRSTUVWXYYZ":
            print(f"'{c}' ist kein gültiger Buchstabe.")
        elif c in misses or c in hits:
            print(f"'{c}' wurde bereits gewählt.")
        else:
            done = True
    return c


while not done:
    print_hangman()
    if hits == wordset:
        print_hangman()
        print("Du hast gewonnen. Gratulation!")
        done = True
    elif len(misses) > 5:
        print_hangman()
        print(f"Du hast leider verloren. Die richtige Lösung lautete: {word}")
        done = True
    else:
        c = read_letter()
        if c in word:
            hits.add(c)
        else:
            misses.append(c)

    if done:
        print()
        ans = input("Möchtest du ein neue Runde spielen? [j/N] ").strip().lower()
        if ans and (ans[0] == "j" or ans[0] == "y"):
            done = False
            word = random.choice(words).upper()
            wordset = set(word)
            hits = set()
            misses = []
        else:
            print("Auf Wiedersehen!")
