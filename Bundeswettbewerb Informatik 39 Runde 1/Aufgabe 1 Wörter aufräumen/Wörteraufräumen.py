import sys
import urllib.request

# Wörter ist eine Liste der Wörter
# Lücken ist eine Liste der Lücken
if len(sys.argv) <= 1:
    # Wenn keine Datei oder Link angegeben wurde,
    # wird die Lösung des ersten Beispiels ausgegeben
    print(
        "Keine Datei oder Link wurde angegeben, hier ist die Lösung des ersten Beispiels"
    )
    url = "https://bwinf.de/fileadmin/bundeswettbewerb/39/raetsel0.txt"
    with urllib.request.urlopen(url) as f:
        Lücken = next(f).decode("utf-8").split()
        Wörter = next(f).decode("utf-8").split()
else:
    if sys.argv[1][:8] == "https://":
        with urllib.request.urlopen(sys.argv[1]) as f:
            Lücken = next(f).decode("utf-8").split()
            Wörter = next(f).decode("utf-8").split()
    else:
        with open(sys.argv[1], encoding="utf-8") as f:
            Lücken = next(f).split()
            Wörter = next(f).split()

# In Satz werden später alle Wörter eingesetzt
Satz = []
# Lückenindex enthält Indizes von Lücken
Lückenindex = {}
# Lückeneinfach enthält eine vereinfachte Form der Lücken
Lückeneinfach = {}
for Index, Lücke in enumerate(Lücken):
    # Die Satzzeichen werden rausgenommen und in Satz gespeichert
    if Lücke[-1] == "_" or Lücke[-1].isalpha():
        Satz += [""]
    else:
        Satz += [Lücke[-1]]
        Lücke = Lücke[:-1]
        Lücken[Index] = Lücke
    # Indizes der Lücken werden zu Lückenindex hinzugefügt
    if Lücke in Lückenindex:
        Lückenindex[Lücke] += [Index]
    else:
        Lückenindex[Lücke] = [Index]
    # Lückeneinfach enthält die Buchstaben mit ihren Indizes der Lücken
    Lückeeinfach = []
    for Index in range(0, len(Lücke)):
        if Lücke[Index] != "_":
            Lückeeinfach += [[Index, Lücke[Index]]]
    Lückeneinfach[Lücke] = Lückeeinfach

# Anzahl enthält die Anzahl jedes Wortes und jeder Lücke
Anzahl = {Wort: Wörter.count(Wort) for Wort in Wörter} | {
    Lücke: Lücken.count(Lücke) for Lücke in Lücken
}
# Wörter und Lücken enthalten nun auch die potenziellen Paare der Wörter und Lücken
Wörter = {Wort: [] for Wort in Wörter}
Lücken = {Lücke: [] for Lücke in Lücken}


def einsetzbar(Wort, Lücke):
    # Sie sind nicht einsetzbar, wenn die Längen unterschiedlich sind
    if len(Wort) != len(Lücke):
        return False
    Lücke = Lückeneinfach[Lücke]
    for Index, Buchstabe in Lücke:
        # Sie sind nicht einsetzbar, wenn ein Buchstabe nicht übereinstimmt
        if Wort[Index] != Buchstabe:
            return False
    # Sie sind einsetzbar, wenn noch nichts zurückgegeben wurde
    return True


def eintragen(Wort):
    # Die Lücke ist ein eindeutiges Paar von dem Wort
    for Lücke in Wörter[Wort]:
        # Das Wort wird in den Endsatz eingesetzt
        for i in range(0, Anzahl[Lücke]):
            Index = Lückenindex[Lücke][i]
            Satz[Index] = Wort + Satz[Index]
        # Die Lücke wird aus dem Dictionary entfernt
        del Lücken[Lücke]


def löschen(Wort):
    # Die Lücke bildet ein eindeutiges Paar mit dem Wort
    for Lücke in Wörter[Wort]:
        # falschesWort bildete ein potenzielles Paar mit der Lücke
        for falschesWort in Lücken[Lücke]:
            if falschesWort != Wort:
                # Die Lücke wird aus den potenziellen Paaren von falschesWort entfernt
                Wörter[falschesWort].remove(Lücke)
                if (
                    sum([Anzahl[Lücke] for Lücke in Wörter[falschesWort]])
                    == Anzahl[falschesWort]
                ):
                    # Wenn die potenziellen Paare von falschesWort jetzt eindeutige Paare sind,
                    # wird die Funktion noch mal mit diesen Paaren/Paar ausgeführt
                    # und falschesWort wird in die Lücken eingesetzt
                    löschen(falschesWort)
                    eintragen(falschesWort)


def aufräumen():
    for Wort in Wörter:
        for Lücke in Lücken:
            # Wenn ein Wort in eine Lücke einsetzbar ist, wird das gespeichert
            if einsetzbar(Wort, Lücke):
                Wörter[Wort] += [Lücke]
                Lücken[Lücke] += [Wort]
        if sum([Anzahl[Lücke] for Lücke in Wörter[Wort]]) == Anzahl[Wort]:
            # Wenn die potenziellen Paare vom Wort eindeutig sind,
            # wird die Löschfunktion aufgerufen und das Wort wird in die Lücken eingesetzt
            löschen(Wort)
            eintragen(Wort)


aufräumen()
# Ergebnisse werden ausgegeben
Satz = " ".join(Satz)
print(Satz)