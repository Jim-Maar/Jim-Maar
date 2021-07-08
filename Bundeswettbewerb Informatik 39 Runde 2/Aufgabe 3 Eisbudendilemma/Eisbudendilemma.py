import sys
import math

# Die Werte in der Eingabedatei werden in Variablen gespeichert
with open(sys.argv[1]) as f:
    Umfang, Anzahl = [int(i) for i in next(f).split()]
    Häuser = [int(i) for i in next(f).split()]

Eisbudenanzahl = int(sys.argv[2])

# dist gibt die Distanz von Punkt1 zu Punkt2 (gegen den Uhrzeigersinn) zurück
def dist(Punkt1, Punkt2):
    if Punkt1 <= Punkt2:
        return Punkt2 - Punkt1
    else:
        return Umfang + Punkt2 - Punkt1


# minplus gibt von zwei Punkten (Punkt2, Punkt3) zurück, welcher von Punkt1 aus weniger gegen den Uhrzeigersinn entfernt ist
def minplus(Punkt1, Punkt2, Punkt3):
    # Wenn die Distanz von Punkt1 zu Punkt2 kleiner ist als die von Punkt1 zu Punkt3,
    # wird Punkt2 zurückgegeben, ansonsten wird Punkt3 zurückgegeben
    if dist(Punkt1, Punkt2) <= dist(Punkt1, Punkt3):
        return Punkt2
    else:
        return Punkt3


# maxplus gibt von zwei Punkten (Punkt2, Punkt3) zurück, welcher von Punkt1 aus mehr im Gegenuhrzeigersinn entfernt ist
def maxplus(Punkt1, Punkt2, Punkt3):
    # Wenn die Distanz von Punkt1 zu Punkt2 größer ist als die von Punkt1 zu Punkt3,
    # wird Punkt2 zurückgegeben, ansonsten wird Punkt3 zurückgegeben
    if dist(Punkt1, Punkt2) >= dist(Punkt1, Punkt3):
        return Punkt2
    else:
        return Punkt3


# verschieben gibt einen Punkt um eine bestimmte Distanz gegen den Uhrzeigersinn verschoben zurück
def verschieben(Punkt, distanz):
    return (Punkt + distanz + Umfang) % Umfang


# gruppen gibt alle Gruppen einer Gruppengröße zurück
def gruppen(n):
    Gruppen = []
    for Index, erstesHaus in enumerate(Häuser):
        letztesHaus = Häuser[(Index + (n - 1)) % Anzahl]
        # Jede Gruppe wird gespeichert mit der Position des letzten Hauses der Gruppe
        # und den Abstand, den die zuletzt platzierte Eisbude zur nächsten Eisbude haben muss,
        # damit die Gruppe sich nicht überlappt
        Gruppen += [[letztesHaus, 2 * dist(erstesHaus, letztesHaus) + 1]]
    return Gruppen


# Die Funktion gruppenbereich gibt das Ende des Gruppenbereiches einer Gruppe zurück
def gruppenbereich(Gruppengröße, Index2, Eisbuden):
    Gruppen = Gruppensammlung[Gruppengröße]
    # BereichEnde wird zuerst auf das letzte Haus der Gruppe gesetzt
    BereichEnde = Gruppen[Index2][0]
    # Eisbudenabstand ist der Abstand, den die zuletzt platzierte Eisbude zur nächsten Eisbude haben muss,
    # damit die Gruppe sich nicht überlappt
    Eisbudenabstand = Gruppen[Index2][1]
    # Wenn sich eine Gruppe über die hälfte des Sees erstreckt,
    # erstreckt sich der Gruppenbereich um den ganzen See
    if Eisbudenabstand <= 0:
        BereichEnde = Eisbuden[0] - 0.5
    else:
        # BereichEnde ist entweder am letzten Haus der Gruppe
        # oder Eisbudenabstand von der zuletzt platzierten Eisbude entfernt,
        # Je nachdem, was weiter gegen den Uhrzeigersinn liegt
        BereichEnde = maxplus(
            Eisbuden[-1], BereichEnde, verschieben(Eisbuden[-1], Eisbudenabstand)
        )
    return BereichEnde


# Die rekursive Funktion varianten erstellt alle Varianten
# Variante ist eine Variante, die für jeden rekursiven Aufruf der Funktion anders ist
# Sie ist zuerst leer, bekommt aber mit jeden tieferem Aufruf eine Höchstüberlappung mehr
# n ist die gewollte Summe der noch fehlenden Höchstüberlappungen und entspricht zu Beginn H//2
# Anzahl ist die Anzahl der noch fehlenden Höchstüberlappungen und entsprich zu Beginn E
def varianten(Variante, n, Anzahl):
    # Die letzte Höchstüberlappung hat die Größe von n
    if Anzahl == 1:
        # Die Basis ist die kleinste Höchstüberlappung
        return [Variante + [n, min(Variante + [n])]]
    # Varianten enthält alle Varianten
    Varianten = []
    # Zu jeder Variante werden alle möglichen Höchstüberlappungen hinzugefügt
    # und für jede wird die Funktion rekursiv aufgerufen
    for i in range(minHöchstüberlappung, n - ((Anzahl - 1) * minHöchstüberlappung) + 1):
        Varianten += varianten(Variante + [i], n - i, Anzahl - 1)
    # Varianten wird ausgegeben
    return Varianten


# minHöchstüberlappung ist die kleinstmögliche Höchstüberlappung
minHöchstüberlappung = math.ceil(math.ceil(Anzahl / 2) / Eisbudenanzahl) - 1

# Gruppensammlung enthält alle Gruppen mit Gruppengrößen 1 Größer als mögliche Höchstüberlappungen
Gruppensammlung = []
for i in range(
    minHöchstüberlappung + 1,
    Anzahl // 2 - (Eisbudenanzahl - 1) * minHöchstüberlappung + 2,
):
    Gruppensammlung += [gruppen(i)]

# Die Varianten werden mit der Funktion varianten erstellt
Varianten = varianten([], Anzahl // 2, Eisbudenanzahl)
# Die Varianten werden ausgegeben
print("Es gibt folgende Varianten:", Varianten)

# nächstesHaus enthält zu jeder Position den Index des Hauses,
# dass sich als Nächstes gegen den Uhrzeigersinn befindet
nächstesHaus = {}
# Zuerst ist der Index 0
Index = 0
# Jede Schrittzahl wird durchgegangen
for i in range(0, Umfang):
    # Wenn die Schrittzahl das nächste Haus erreicht, wird der Index erhöht
    if i == Häuser[Index % Anzahl]:
        Index += 1
    # Der Index wird zur Position eingetragen
    nächstesHaus[i] = Index

# Die Funktion eisbudendilemma findet stabile Eisbudenstandorte
def eisbudendilemma():
    # Jedes Haus und Variante werden durchgegangen, die erste Eisbude wird auf das Haus gesetzt
    for Index, Haus in enumerate(Häuser):
        for Variante in Varianten:
            Eisbuden = [Haus]
            Basis = Variante[Eisbudenanzahl]
            # Start und Ende sind die Indices der ersten Häuser der ersten und letzten Gruppe,
            # dessen Gruppenbereiche nach der ersten Eisbude erstellt werden
            Start = Index + 1
            Ende = Start + Basis + 1
            # Es werden E Eisbuden gesetzt
            for i in range(0, Eisbudenanzahl):
                # Höchstüberlappung ist die Höchstüberlappung nach der letzten Eisbude, die platziert wurde
                Höchstüberlappung = Variante[i]
                # BereichEnde ist das Ende eines Bereiches, dass sich weiter gegen den Uhrzeigersinn befindet
                # MinBereichEnde ist das BereichEnde, das sich am wenigstem gegen den Uhrzeigersinn befindet
                MinBereichEnde = Eisbuden[-1] - 0.5
                # Alle Gruppen mit der Größe Höchstüberlappung von den Höchstüberlappung + Basis Häusern
                # Nach der zuletzt platzierten Eisbude werden durchgegangen
                # Index2 ist der Index der jeweiligen Gruppe
                for Index2 in range(Start, Ende):
                    Index2 %= Anzahl
                    # Das Ende des Gruppenbereichs wird bestimmt
                    BereichEnde = gruppenbereich(
                        Höchstüberlappung - minHöchstüberlappung, Index2, Eisbuden
                    )
                    # Wenn BereichEnde sich weniger gegen den Uhrzeigersinn befindet
                    # als das bisherige MinBereichEnde, wird dieses nun angepasst
                    if dist(Eisbuden[-1], BereichEnde) < dist(
                        Eisbuden[-1], MinBereichEnde
                    ):
                        MinBereichEnde = BereichEnde
                # Die nächste Eisbude wird entweder beim MinbereichEnde oder am Haus,
                # dass Höchstüberlappung + Basis + 1 Häuser von der zuletzt platzierten Eisbude entfernt liegt, platziert
                # Je nachdem, welcher Punkt weniger gegen den Uhrzeigersinn liegt
                Eisbuden += [
                    minplus(
                        Eisbuden[-1],
                        MinBereichEnde,
                        Häuser[(Start + Höchstüberlappung + Basis) % Anzahl],
                    )
                ]
                # Start ist der Index vom ersten Haus nach der eben platzierten Eisbude
                # Ende ist Basis + 1 Häuser dahinter
                Start = nächstesHaus[Eisbuden[-1]]
                Ende = Start + Basis + 1
            # Wenn die letzte Eisbude von der ersten Eisbude aus vor der vorletzten Eisbude liegt,
            # sind die Eisbudenpositionen stabil und sie werden ohne die letzte Eisbude ausgegeben
            if dist(Eisbuden[0], Eisbuden[-1]) < dist(Eisbuden[0], Eisbuden[-2]):
                return Eisbuden[:-1]


# Die Lösung wird ausgegeben
Eisbuden = eisbudendilemma()
if Eisbuden:
    print("Die zuerst gefundenen stabilen Eisbudenstandorte lauten:", Eisbuden)
else:
    print("Es gibt keine stabilen Eisbudenstandorte")