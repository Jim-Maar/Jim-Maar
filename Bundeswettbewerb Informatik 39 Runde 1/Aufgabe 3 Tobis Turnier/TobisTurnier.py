import urllib.request
import sys
from math import log
import random

Stärken = []
# n ist die Anzahl der Spieler
# Stärken beinhaltet die Stärke von jedem Spieler
if len(sys.argv) <= 1:
    # Wenn keine Datei oder Link angegeben wurde,
    # wird die Lösung des ersten Beispiels ausgegeben
    print(
        "Keine Datei oder Link wurde angegeben, hier ist die Lösung des ersten Beispiels"
    )
    url = "https://bwinf.de/fileadmin/bundeswettbewerb/39/spielstaerken1.txt"
    with urllib.request.urlopen(url) as f:
        n = int(next(f))
        for stärke in f:
            Stärken += [int(stärke.decode("utf-8"))]
else:
    if sys.argv[1][:8] == "https://":
        with urllib.request.urlopen(sys.argv[1]) as f:
            n = int(next(f))
            for stärke in f:
                Stärken += [int(stärke.decode("utf-8"))]
    else:
        with open(sys.argv[1]) as f:
            n = int(next(f))
            for stärke in f:
                Stärken += [int(stärke)]


def Spielersortieren():
    # Stärkeindeces enthält für jede Stärke die Personen, die diese Stärke haben
    Stärkeindices = dict(zip(Stärken, [[] for _ in range(n)]))
    for Spieler, Stärke in enumerate(Stärken):
        Stärkeindices[Stärke] += [Spieler]
    # Stärken2 enthält alle Stärken sortiert
    Stärken2 = Stärken.copy()
    Stärken2.sort()
    Stärken2.reverse()
    return [Stärkeindices[Stärke].pop(0) for Stärke in Stärken2]


# Spieler enthält alle Spieler sortiert nach ihrer Stärke,
# für die Erstellung wird die Funktion Spielersortieren benutzt
Spieler = Spielersortieren()

# besterSpieler ist die Spielernummer des spielstärksten Spielers
besterSpieler = Spieler[0]
# Durchgänge ist die Anzahl an Turnieren, die simuliert werden
durchgänge = 100000


def Wahrscheinlichkeitskampf(Spieler1, Spieler2, fünf):
    # Stärke1 und 2 sind die Stärken der Spieler
    Stärke1 = Stärken[Spieler1]
    Stärke2 = Stärken[Spieler2]
    # P1 und P2 sind Gewinnwahrscheinlichkeiten der Spieler
    P1 = Stärke1 / (Stärke1 + Stärke2)
    P2 = 1 - P1
    if fünf:
        # Bei KO5 wird die Formel auf sie angewandt
        P1 = P1 ** 3 * (1 + 3 * P2 + 6 * P2 ** 2)
        P2 = 1 - P1
    # Doe Gewinnwahrscheinlichkeit beider Spieler wird zurückgegeben
    return P1, P2


def kampf(Spieler1, Spieler2):
    # Der Spieler, der den Kampf gewinnt, wird zurückgegeben
    if random.random() <= Gewinnwahrscheinlichkeiten[Spieler1][Spieler2]:
        return Spieler1
    return Spieler2


def vorrechnen(fünf):
    Gewinnwahrscheinlichkeiten = n * [0]
    Gewinnwahrscheinlichkeiten = [n * [i] for i in Gewinnwahrscheinlichkeiten]
    for Spieler1 in range(0, n):
        for Spieler2 in range(Spieler1 + 1, n):
            # Bei KO5 werden die Gewinnwahrscheinlichkeiten mit der Formel ausgerechnet
            # Ansonsten normal
            P1, P2 = Wahrscheinlichkeitskampf(Spieler1, Spieler2, fünf)
            # Die Gewinnwahrscheinlichkeiten von allen Paaren an Spielern werden eingetragen
            Gewinnwahrscheinlichkeiten[Spieler1][Spieler2] = P1
            Gewinnwahrscheinlichkeiten[Spieler2][Spieler1] = P2
    return Gewinnwahrscheinlichkeiten


# Liga
def Liga():
    # Ligagewinne speichert die Gewinne jedes Spielers
    Ligagewinne = n * [0]
    for index, Spieler1 in enumerate(Spieler):
        for Spieler2 in Spieler[index + 1 :]:
            # Jeder Spieler kämpft gegen jeden anderen Spieler
            Ligagewinne[kampf(Spieler1, Spieler2)] += 1
        # Wenn ein Spieler mehr Siege hat als der beste Spieler
        # oder genau gleich viele mit einer niedrigeren Nummer hat der beste Spieler verloren
        # Es wird also eine 0 zurückgegeben
        if Spieler1 != besterSpieler and (
            Ligagewinne[Spieler1] > Ligagewinne[besterSpieler]
            or (
                Ligagewinne[Spieler1] == Ligagewinne[besterSpieler]
                and Spieler1 <= besterSpieler
            )
        ):
            return 0
    # Wenn das nie zugetroffen ist, hat er gewonnen. Es wird also eine 1 zurückgegeben
    return 1


# K.O.
def KORunde(Spieler):
    # nächsteSpieler beinhaltet die Spieler, die weiter kommen
    nächsteSpieler = []
    # Jeder Spieler kämpft gegen einen anderen Spieler, die Gewinner kommen in die Liste
    for i in range(0, len(Spieler), 2):
        Spieler1 = Spieler[i]
        Spieler2 = Spieler[i + 1]
        nächsteSpieler += [kampf(Spieler1, Spieler2)]
    # nächsteSpieler wird zurückgegeben
    return nächsteSpieler


def KORunde2(Plätze, Wahrscheinlichkeiten):
    #  Wahrscheinlichkeitenneu beinhaltet die Wahrscheinlichkeit, jedes Spielers weiter zu kommen
    Wahrscheinlichkeitenneu = n * [0]
    # Plätzeneu beinhaltet die nächsten Plätze
    Plätzeneu = []
    # Jeder Spieler auf einem Platz kämpft gegen einen jeden Spieler aus einem anderen Platz
    for i in range(0, len(Plätze), 2):
        Platz1 = Plätze[i]
        Platz2 = Plätze[i + 1]
        # Alle Spieler aus den beiden Plätzen kommen dann in einen Platz
        # Wenn der beste Spieler kämpft, kommt nur er weiter
        if i == 0:
            Plätzeneu += [Platz1]
        else:
            Plätzeneu += [Platz1 + Platz2]
        for Spieler1 in Platz1:
            for Spieler2 in Platz2:
                # Basiswahrscheinlichkeit ist die Wahrscheinlichkeit,
                # dass die beiden Spieler gegeneinander kämpfen
                # Sie ist das Produkt der momentanen Wahrscheinlichkeiten, der beiden Spieler
                Basiswahrscheinlichkeit = (
                    Wahrscheinlichkeiten[Spieler1] * Wahrscheinlichkeiten[Spieler2]
                )
                # P1 und P2 sind Wahrscheinlichkeiten, dass der jeweilige Spieler gewinnt
                # Das Produkt der beiden ist die Wahrscheinlichkeit, dass der Spieler weiter kommt
                # Sie wird zu Wahrscheinlichkeitenneu hinzugefügt
                P1 = Gewinnwahrscheinlichkeiten[Spieler1][Spieler2]
                Wahrscheinlichkeitenneu[Spieler1] += Basiswahrscheinlichkeit * P1
                # Die Gewinnwahrscheinlichkeiten gegen den besten Spieler werden nicht gebraucht
                if i != 0:
                    P2 = Gewinnwahrscheinlichkeiten[Spieler2][Spieler1]
                    Wahrscheinlichkeitenneu[Spieler2] += Basiswahrscheinlichkeit * P2
    # Die neuen Plätze und Wahrscheinlichkeiten werden zurückgegeben
    return Plätzeneu, Wahrscheinlichkeitenneu


def KO():
    # KOSpieler beinhaltet alle Spieler, die noch im Spiel sind, in einer zufälligen Reihenfolge
    # Der beste Spieler ist aber immer das erste Element
    KOSpieler = list(range(0, n))
    KOSpieler.pop(besterSpieler)
    random.shuffle(KOSpieler)
    KOSpieler = [besterSpieler] + KOSpieler
    # Alle Runden werden durchgegangen, bis nur noch 8 Spieler im Spiel sind
    for _ in range(3, int(log(n, 2))):
        # Jeder Spieler kämpft ein Mal, die Verlierer fliegen raus
        KOSpieler = KORunde(KOSpieler)
        # Wenn der beste Spieler raus ist, hat er eine Turniersiegwahrscheinlichkeit von 0
        if KOSpieler[0] != besterSpieler:
            return 0
    # KOSpieler wird in Platzform gebracht
    KOPlätze = [[i] for i in KOSpieler]
    # Wahrscheinlichkeiten beinhaltet die Wahrscheinlichkeiten aller Spieler,
    # dass sie auf dem jetzigen Platz sind
    Wahrscheinlichkeiten = n * [1]
    # Die zweite KO Funktion wird durchgeführt, bis nur noch ein Platz übrig ist
    for _ in range(0, 3):
        KOPlätze, Wahrscheinlichkeiten = KORunde2(KOPlätze, Wahrscheinlichkeiten)
    # Die Turniersiegwahrscheinlichkeit des besten Spielers wird zurückgegeben
    return Wahrscheinlichkeiten[besterSpieler]


# Gewinnwahrscheinlichkeiten enthält die Gewinnwahrscheinlichkeiten
# von jedem Spieler gegen jeden anderen Spieler
Gewinnwahrscheinlichkeiten = vorrechnen(False)
# Gewinne beihaltet die Anzahl an Turniersiegen von dem besten Spieler
Gewinne = 0
# Das Turnier wird viele Male simuliert
# Liga gibt 1 für einen Sieg und 0 für eine Niederlage des besten Spielers zurück
for _ in range(0, durchgänge):
    Gewinne += Liga()
# Die Gewinne werden durch die Anzahl der Durchgänge geteilt und mal 100
# genommen Turniergewinnwahrscheinlichkeit in Prozent zu erhalten
# Da es sich um eine Simulation handelt, wird die Wahrscheinlichkeit gerundet
print(f"Liga: {round(Gewinne / durchgänge * 100, 2)}%")

# Mit KO und KO5 wird das Gleiche gemacht
# Bei KO/KO5 bekommt der beste Spieler eine Turniergewinnwahrscheinlichkeit
# Diese wird in Gewinne eingetragen
Gewinne = 0
for _ in range(0, durchgänge):
    Gewinne += KO()
print(f"K.O.: {round(Gewinne / durchgänge * 100, 2)}%")

# Bei KO5 werden die Gewinnwahrscheinlichkeiten mit der Formel berechnet
Gewinnwahrscheinlichkeiten = vorrechnen(True)
Gewinne = 0
for _ in range(0, durchgänge):
    Gewinne += KO()
print(f"K.O. x5: {round(Gewinne / durchgänge * 100, 2)}%")