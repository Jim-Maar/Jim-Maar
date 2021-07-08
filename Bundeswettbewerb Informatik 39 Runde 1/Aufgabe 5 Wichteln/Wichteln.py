import urllib.request
import math
import sys

# n ist die Anzahl an Personen
# Wünscheliste ist eine Liste der Wünsche aller Personen
Wünscheliste = []
if len(sys.argv) <= 1:
    # Wenn keine Datei oder Link angegeben wurde,
    # wird die Lösung des ersten Beispiels ausgegeben
    print(
        "Keine Datei oder Link wurde angegeben, hier ist die Lösung des ersten Beispiels"
    )
    url = "https://bwinf.de/fileadmin/bundeswettbewerb/39/wichteln1.txt"
    with urllib.request.urlopen(url) as f:
        n = int(next(f))
        for wünsche in f:
            Wünscheliste += [[int(i) for i in wünsche.decode("utf-8").split()]]
else:
    if sys.argv[1][:8] == "https://":
        with urllib.request.urlopen(sys.argv[1]) as f:
            n = int(next(f))
            for wünsche in f:
                Wünscheliste += [[int(i) for i in wünsche.decode("utf-8").split()]]
    else:
        with open(sys.argv[1]) as f:
            n = int(next(f))
            for wünsche in f:
                Wünscheliste += [[int(i) for i in wünsche.split()]]

# Verteilung wird die gesuchte beste Verteilung sein
verteilung = n * [0]


def löschen(Wünsche, Person):
    # Gegenstand ist der Gegenstand
    Gegenstand = sum(Wünsche)
    # Wunschgrad ist der Wunschgrad von dem Gegenstand
    Wunschgrad = Wünsche.index(Gegenstand)
    # Indizes beinhaltet alle Personen, die sich den Gegenstand wünschen
    Indizes = [Personen[Wunschgrad][Gegenstand]]
    # Personen wird aktualisiert, der Wunsch wird nur von einer Person gewünscht
    Personen[Wunschgrad][Gegenstand] = [Person]
    if Wunschgrad == 1 and Gegenstand in Personen[2]:
        # Bei einem Wunschgrad von 2 werden auch Wünsche mit Wunschgrad 3 gelöscht
        Indizes += [Personen[2][Gegenstand]]
        del Personen[2][Gegenstand]
    for index in range(0, len(Indizes)):
        for Person2 in Indizes[index]:
            Wünsche2 = Wünscheliste[Person2]
            if Person != Person2:
                # Der Wunsch wird von anderen Personen entfernt
                Wünsche2[Wunschgrad + index] = 0
                # Die Funktion wird noch mal aufgerufen,
                # wenn die Person nur noch einen Wunsch hat
                if Wünsche2.count(0) == 2:
                    löschen(Wünsche2, Person2)


def indextoWunsch(index, Wunschgrad):
    # Wunschgrad ist der Wunschgrad, für den grade Varianten erstellt werden
    # Wünsche sind die Wünsche einer Person
    Wünsche = Wünscheliste[index]
    # Alle Wünsche mit einem höheren Wunschgrad werden zurückgegeben
    if Wünsche[Wunschgrad + 1] != 0:
        yield [Wunschgrad + 1, Wünsche[Wunschgrad + 1]]
    if Wunschgrad == 0 and Wünsche[Wunschgrad + 2] != 0:
        yield [Wunschgrad + 2, Wünsche[Wunschgrad + 2]]


def Verteilungenerstellung(locPersonen, Wunschgrad):
    # locPersonen2 beinhaltet alle gewünschten Gegenstände und die Personen
    locPersonen2 = {k: v for (k, v) in locPersonen[Wunschgrad].items() if len(v) >= 1}
    # Personensammlung wird alle Verteilungen beinhalten
    Personensammlung = []
    if len(locPersonen2) > 0:
        # Gegenstandliste beinhaltet alle gewünschten Gegenstände als Liste
        Gegenstandliste = [k for (k, v) in locPersonen2.items()]

        def Verteilungenerstellung2(Gegenstandindex, locPersonen):
            nonlocal Personensammlung
            # Gegenstand ist ein gewünschter Gegenstand
            Gegenstand = Gegenstandliste[Gegenstandindex]
            # Indizes sind Personen, die sich diesen Gegenstand Wünschen
            Indizes = locPersonen2[Gegenstand]
            for index in Indizes:
                # Für jede dieser Personen wird die Verteilung kopiert
                locPersonen3 = [
                    {k: v.copy() for (k, v) in i.items()} for i in locPersonen
                ]
                # Der Gegenstand wird in dieser Verteilung nur von der Person gewünscht
                locPersonen3[Wunschgrad][Gegenstand] = [index]
                # Die anderen Wünsche der Person werden aus der Verteilung gelöscht
                for Wunschgrad2, Gegenstand2 in indextoWunsch(index, Wunschgrad):
                    locPersonen3[Wunschgrad2][Gegenstand2].remove(index)
                    if len(locPersonen3[Wunschgrad2][Gegenstand2]) == 0:
                        del locPersonen3[Wunschgrad2][Gegenstand2]
                if Gegenstandindex + 1 < len(Gegenstandliste):
                    # Aus dieser Verteilung werden weitere Verteilungen erstellt,
                    # in denen andere Gegenstände erhalten werden
                    Verteilungenerstellung2(Gegenstandindex + 1, locPersonen3)
                else:
                    # Wenn es keine weiteren Gegenstände mehr gibt,
                    # wird die Verteilung zu Personensammlung hinzugefügt
                    Personensammlung += [locPersonen3]

        # Verteilungenerstellung2 erstellt alle weiteren Verteilung
        Verteilungenerstellung2(0, locPersonen)
    else:
        # Wenn keine weiteren Verteilungen erstellt werden,
        # wird die eingegebene Verteilung zurückgegeben
        Personensammlung += [locPersonen]
    return Personensammlung


Erstwünsche = [i[0] for i in Wünscheliste]
for Wunschgrad in range(1, 3):
    for Person, Wünsche in enumerate(Wünscheliste):
        # Wünsche mit Wunschgrad 2 und 3 von Gegenständen mit Wunschgrad 1 werden gelöscht
        if Wünsche[Wunschgrad] in Erstwünsche:
            Wünscheliste[Person][Wunschgrad] = 0

# Personen enthält zu jedem Gegenstand die Personen, die ihn Wünschen sortiert nach Wunschgrad
Personen = [{}, {}, {}]
for Wunschgrad in range(0, 3):
    for Person, Wünsche in enumerate(Wünscheliste):
        # Alle Personen, die nicht gelöscht wurden, werden in Personen gespeichert
        if Wünsche[Wunschgrad] != 0:
            if Wünsche[Wunschgrad] not in Personen[Wunschgrad]:
                Personen[Wunschgrad][Wünsche[Wunschgrad]] = [Person]
            else:
                Personen[Wunschgrad][Wünsche[Wunschgrad]] += [Person]

# Für jede Person, die einen einzigen Gegenstand wünscht, wird die Löschfunktion aktiviert
for Person, Wünsche in enumerate(Wünscheliste):
    if Wünsche.count(0) == 2:
        # Die Löschfunktion löscht Wünsche von Gegenständen die unnötig sind,
        # weil eine Person eh nur diesen Gegenstand erhalten kann
        löschen(Wünsche, Person)

# Personensammlung beinhaltet alle möglichen Variationen von erfüllten ErstWünschen
Personensammlung = Verteilungenerstellung(Personen, 0)

for Personen in Personensammlung:
    # Gegenstände mit Wunschgrad 3 werden aus einer Verteilung rausgenommen,
    # wenn sie mit Wunschgrad 2 erfüllt werden können
    Personen[2] = {k: v for (k, v) in Personen[2].items() if k not in Personen[1]}

# Personensammlung2 enthält alle möglichen sinnvollen Variationen von erfüllten ZweitWünschen
Personensammlung2 = []
# maxlen ist die größte Anzahl an erfüllbaren ZweitWünschen,
# bei Erfüllung der größtmöglichen Anzahl an ErstWünschen
maxlen = max(len(i[1]) for i in Personensammlung)
for Personen in Personensammlung:
    if len(Personen[1]) == maxlen:
        # Wenn die Anzahl an erfüllbaren ZweitWünschen einer Verteilung gleich maxlen ist,
        # werden alle Variationen von erfüllten ZweitWünschen zu dieser Verteilung erstellt
        Personensammlung2 += Verteilungenerstellung(Personen, 1)

# restGegenstände enthält Gegenstände, die niemand erhalten hat
# Sie beeinflussen nicht die Bewertung
restGegenstände = list(range(1, n + 1))
# maxlen ist die größte Anzahl an erfüllbaren DrittWünschen,
# bei Erfüllung der größtmöglichen Anzahl an Erst- und ZweitWünschen
maxlen = max(len(i[2]) for i in Personensammlung2)
for Personen in Personensammlung2:
    # Die Verteilung mit den meisten erfüllbaren DrittWünschen,
    # wird in Listenform gebracht
    if len(Personen[2]) == maxlen:
        for Wunschgrad in Personen:
            for Gegenstand in Wunschgrad:
                verteilung[Wunschgrad[Gegenstand][0]] = Gegenstand
                # Erfüllte Wünsche werden aus restGegenstände entfernt
                restGegenstände[Gegenstand - 1] = 0
        break
# Die restGegenstände werden in das Endergebnis eingesetzt
restGegenstände = [i for i in restGegenstände if i != 0]
verteilung = [i if i != 0 else restGegenstände.pop(0) for i in verteilung]
# Das Ergebnis wird ausgegeben
print(verteilung)