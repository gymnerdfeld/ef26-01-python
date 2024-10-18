# Ein int bei der:m Benutzer:in abfragen

done = False
while not done:
    answer = input("Wie alt bist du? ")
    if answer.isdigit():
        age = int(answer)
        print(f"Dann wirst du nächstes Jahr {age + 1}")
        done = True
    else:
        print("Ungültige Eingabe")


# Zusatzaufgabe
def input_int(prompt):
    while True:
        answer = input(prompt)
        if answer.isdigit():
            return int(answer)
        else:
            print("Ungültige Eingabe")


age = input_int("Wie alt bist du? ")
print(f"Dann wirst du nächstes Jahr {age + 1}")


# Zusatzaufgabe 2
def isdigit(text):
    for c in text:
        if c not in "0123456789":
            return False
    return True


# Zusatzaufgabe 3
def input_choice(prompt, choice):
    while True:
        answer = input(prompt)
        if answer in choice:
            return answer
        else:
            print("Ungültige Eingabe")


print("Was ist keine Frucht?")
print("A: Tomaten")
print("B: Melonen")
print("C: Kokosnuss")
answer = input_choice("> ", ["A", "B", "C"])
if answer == "C":
    print("Korrekt!")
else:
    print("Leider falsch")
