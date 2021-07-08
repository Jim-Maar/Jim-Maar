import sys

# Die Werte in der Eingabedatei werden in Variablen gespeichert
with open(sys.argv[1]) as f:
    Anzahl = int(next(f))
    Wunschobst = set([i for i in next(f).split()])
    n = int(next(f))
    Obstspieße = []
    Schüsseln = []
    for _ in range(0, n):
        Schüsseln += [{int(i) for i in next(f).split()}]
        Obstspieße += [{i for i in next(f).split()}]

# Schüsselmengen enthält am Anfang S0, also die Menge aller Schüsseln
Schüsselmengen = [{i for i in range(1, Anzahl + 1)}]
# Obstmengen enthält am Anfang O0, also das Wunschobst
Obstmengen = [Wunschobst.copy()]
# Zielmenge ist die Menge, in der Wunschobst zu finden ist
Zielmenge = []

# Jede Person wird durchgegangen
for index in range(0, n):
    # SchüsselmengeP ist die Schüsselmenge der Person
    SchüsselmengeP = Schüsseln[index]
    # ObstmengeP ist die Obstmenge der Person
    ObstmengeP = Obstspieße[index]
    # Während über die Obst- und Schüsselmengen iteriert wird, werden Mengen hinzugefügt
    # Dafür werden Kopien der Listen Schüsselmengen und Obstmengen gemacht
    Schüsselmengenkopie = Schüsselmengen.copy()
    Obstmengenkopie = Obstmengen.copy()
    Schüsselmengen = []
    Obstmengen = []
    # Jede Obst- und Schüsselmenge in M wird durchgegangen
    for index2 in range(0, len(Obstmengenkopie)):
        Obstmenge = Obstmengenkopie[index2]
        Schüsselmenge = Schüsselmengenkopie[index2]
        # Die Obstmenge wird durch die Schnittmenge mit der Obstmenge der Person ersetzt
        Obstmengeneu = Obstmenge.intersection(ObstmengeP)
        if len(Obstmengeneu) != 0:
            # Dasselbe wird mit der Schüsselmenge und der Schüsselmenge der Person gemacht
            Schüsselmengeneu = Schüsselmenge.intersection(SchüsselmengeP)
            # Wenn beide Mengen gleich groß sind, wird die neue Schüsselmenge zur Zielmenge hinzugefügt
            # Ansonsten werden die Mengen zu den Obst- und Schüsselmengen hinzugefügt
            if len(Schüsselmengeneu) == len(Obstmengeneu):
                Zielmenge += [Schüsselmengeneu]
            else:
                Obstmengen += [Obstmengeneu]
                Schüsselmengen += [Schüsselmengeneu]

        # Des Weiteren wird die Differenzmenge mit der Obstmenge der Person erstellt
        Obstmengeneu = Obstmenge.difference(ObstmengeP)
        if len(Obstmengeneu) != 0:
            # Dasselbe wird mit der Schüsselmenge und der Schüsselmenge der Person gemacht
            Schüsselmengeneu = Schüsselmenge.difference(SchüsselmengeP)
            # Wenn beide Mengen gleich groß sind, wird die neue Schüsselmenge zur Zielmenge hinzugefügt
            # Ansonsten werden die Mengen zu den Obst- und Schüsselmengen hinzugefügt
            if len(Schüsselmengeneu) == len(Obstmengeneu):
                Zielmenge += [Schüsselmengeneu]
            else:
                Obstmengen += [Obstmengeneu]
                Schüsselmengen += [Schüsselmengeneu]

# Aufzählung gibt eine Aufzählung der Elemente einer Menge als String zurück
def Aufzählung(Menge, Wort):
    Menge = list(Menge)
    if len(Menge) == 1:
        return Menge[0]
    else:
        Text = ""
        for i in range(0, len(Menge) - 1):
            Text += str(Menge[i]) + ", "
        Text = Text[:-2] + Wort + str(Menge[i + 1])
        return Text


# Wenn alle Obstmengen Teilzielmengen wurden, wird die Zielmenge ausgegeben
if len(Obstmengen) == 0:
    print(
        "Die Menge der Schüsseln, in denen die Wunschsorten zu finden sind, lautet:",
        set.union(*Zielmenge),
    )
else:
    # Ansonsten wird zu jeder Obstmenge, die keine Teilzielmengen sind,
    # die zugehörige Schüsselmenge ausgegeben
    for index in range(0, len(Obstmengen)):
        Obstmenge = Obstmengen[index]
        Schüsselmenge = Schüsselmengen[index]
        if len(Obstmenge) == 1:
            wort1 = ""
            wort2 = "ist"
        else:
            wort1 = "n"
            wort2 = "sind"
        print(
            f"Die Wunschsorte{wort1} {Aufzählung(Obstmenge,' und ')} {wort2} in den Schüsseln {Aufzählung(Schüsselmenge, ' oder ')} zu finden."
        )
    # Es wird außerdem der Teil der Zielmenge ausgegeben, der bestimmt werden kann
    if len(Zielmenge) == 1:
        print(
            f"Die andere Wunschsorte ist in der Schüssel {Aufzählung(set.union(*Zielmenge), ' und ')} zu finden."
        )
    elif len(Zielmenge) > 1:
        print(
            f"Die anderen Wunschsorten sind in den Schüsseln {Aufzählung(set.union(*Zielmenge), ' und ')} zu finden."
        )