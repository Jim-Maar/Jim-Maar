Vorher0 = {
    0: [[0, 0, 0, 0], [0, 0, 2, 0]],
    60: [[0, 0, 2, 0]],
    90: [[0, 0, 0, 0], [2, 0, 0, 0], [1, 0, 2, 1]],
    120: [[2, 0, 2, 0]],
}
Nachher0 = {
    0: [],
    60: [[0, 0, 0, 0], [0, 0, 2, 0]],
    90: [[0, 0, 0, 0], [2, 0, 0, 0], [1, 0, 0, 1]],
    120: [[2, 0, 0, 0], [2, 0, 2, 0]],
}
Vorher1 = {
    30: [[0, 0, 0, 0], [0, 0, 2, 0], [0, 1, 1, 0]],
    90: [[0, 0, 0, 0], [0, 0, 2, 0], [0, 1, 1, 0]],
    150: [[0, 1, 1, 0], [0, 2, 2, 0], [0, 1, 3, 0]],
}
Nachher1 = {
    30: [[0, 0, 0, 0], [0, 0, 2, 0], [0, 1, -1, 0]],
    90: [[0, 0, 0, 0], [0, 2, 0, 0], [0, 1, 1, 0]],
    150: [[0, 2, 2, 0], [0, 2, 0, 0], [0, 1, -1, 0]],
}
Vorher2 = {
    0: [[1, 0, 0, 1], [3, 0, 0, 1], [1, 0, 2, 1], [3, 0, 2, 1]],
    30: [[1, -1, 1, 1], [5, 0, 0, 1]],
    60: [[0, 0, 0, 0], [4, 0, 0, 0]],
    90: [[1, 0, 0, 1], [5, 0, 0, 1]],
    120: [[2, 0, 0, 0], [6, 0, 0, 0], [5, 0, 2, 1]],
    150: [[5, 1, 1, 1]],
}
Nachher2 = {
    0: [[1, 0, 0, 1], [3, 0, 0, 1], [1, 0, 2, 1], [3, 0, 2, 1]],
    30: [[5, -1, 1, 1]],
    60: [[0, 0, 0, 0], [4, 0, 0, 0]],
    90: [[1, 0, 0, 1], [5, 0, 0, 1]],
    120: [[2, 0, 0, 0], [6, 0, 0, 0], [5, 0, 2, 1]],
    150: [[5, 0, 0, 1], [1, 0, 2, 1]],
}
Vorher3 = {
    30: [[0, 0, 0, 0], [0, 1, -1, 0], [0, 2, 0, 0], [0, 3, -1, 0]],
    60: [[0, 2, 0, 0], [-1, 2, 0, 1], [-1, 2, 0, -1], [0, 2, 0, -2]],
    120: [[0, 2, 0, 0], [1, 2, 0, 1], [1, 2, 0, -1], [0, 2, 0, -2]],
    150: [[0, 1, -1, 0], [0, 2, 0, 0], [0, 3, -1, 0], [0, 4, 0, 0]],
}
Nachher3 = {
    0: [[2, 0, 0, 2], [0, 0, 0, 2]],
    30: [[2, 0, 0, 2], [2, -1, -1, 2]],
    60: [[0, 0, 0, 0], [1, 0, 0, 1], [2, 0, 0, 2]],
    90: [[2, 0, 0, 2], [2, 0, -2, 2], [2, 0, -4, 2], [2, 0, 2, 2]],
    120: [[2, 0, 0, 2], [4, 0, 0, 0], [3, 0, 0, 1]],
    150: [[2, 0, 0, 2], [2, 1, -1, 2]],
}
Vorher4 = {
    0: [
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [4, 0, 0, 0],
        [6, 0, 0, 0],
        [0, 0, 2, 0],
        [2, 0, 2, 0],
        [4, 0, 2, 0],
        [4, 0, -2, 0],
        [6, 0, -2, 0],
    ],
    90: [
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [4, 0, 0, 0],
        [6, 0, 0, 0],
        [4, 0, -2, 0],
        [6, 0, -2, 0],
        [8, 0, -2, 0],
    ],
}
Nachher4 = {
    0: [
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [4, 0, 0, 0],
        [6, 0, 0, 0],
        [0, 0, 2, 0],
        [4, 0, 2, 0],
        [2, 0, -2, 0],
        [6, 0, -2, 0],
    ],
    90: [
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [4, 0, 0, 0],
        [6, 0, 0, 0],
        [2, 0, -2, 0],
        [4, 0, -2, 0],
        [6, 0, -2, 0],
        [8, 0, -2, 0],
    ],
}
Vorher5 = {
    30: [[0, 0, 0, 0], [0, 1, 1, 0], [0, 2, 2, 0]],
    90: [[0, 1, -1, 0], [0, 1, 1, 0], [0, 1, 3, 0]],
    150: [[0, 1, 3, 0], [0, 2, 2, 0], [0, 3, 1, 0]],
}
Nachher5 = {
    30: [[0, 0, 0, 0], [0, 0, 2, 0], [0, 1, 1, 0]],
    90: [[0, 0, 0, 0], [0, 0, 2, 0], [0, 1, 1, 0]],
    150: [[0, 1, 1, 0], [0, 2, 2, 0], [0, 1, 3, 0]],
}

import sys

# Vorher ist die Streichholzanordnung,
# die in die Streichholzanordnung Nachher überführt werden soll
# Beide Streichholzanordnungen müssen gleich lang sein
# u ist die Anzahl der Streichhölzer, die umgelegt werden sollen
if len(sys.argv) < 4:
    # Wenn nicht genug Parameter angegeben wurden,
    # wird eine Lösung des ersten Beispiels ausgegeben
    print(
        "Nicht genug Parameter wurden angegeben, hier ist eine Lösung des ersten Beispiels"
    )
    Vorher = Vorher0
    Nachher = Nachher0
    u = 3
else:
    Vorher = sys.argv[1]
    Nachher = sys.argv[2]
    u = sys.argv[3]
    exec("Vorher = " + Vorher)
    exec("Nachher = " + Nachher)
    exec("u = " + u)
# n ist die Anzahl der Streichhölzer in Vorher/Nachher
n = sum([len(v) for v in Vorher.values()])


# Implementierung von Subtraktion von Punkten/Vektoren
def vektorMinus(vektor1, vektor2):
    return [vektor1[index] - vektor2[index] for index in range(0, 4)]


def übereinanderlegen(Vektor):
    def ausgeben(UmzulegendVorher, UmzulegendNachher):
        if u == umzulegend + 1:
            # Wenn es ein umzulegendes Streichholz weniger gibt als u,
            # Wird ein passendes Streichholz statt einem umzulegenden umgelegt
            UmzulegendVorher[passendesStreichholz[1]] += [passendesStreichholz[0]]
            UmzulegendVorher[umzulegendesStreichholz[1]].remove(
                umzulegendesStreichholz[0]
            )
        # UmzulegendVorher und UmzulegendNachher werden gekürzt
        UmzulegendVorher = {k: v for (k, v) in UmzulegendVorher.items() if len(v) > 0}
        UmzulegendNachher = {k: v for (k, v) in UmzulegendNachher.items() if len(v) > 0}
        # Die umzulegenden Streichhölzer von Vorher werden auf die von Nachher gelegt
        Lösung = f"Das Rätsel ist lösbar.\nDie {umzulegend} Streichhölzer an folgenden Positionen:\n{UmzulegendVorher}\nwerden an diese Positionen verschoben und gedreht\n{UmzulegendNachher}."
        # Die Lösung wird ergänzt, wenn es weniger umzulegende Streichhölzer gibt als u
        if u == umzulegend + 1:
            # Wenn es ein umzulegendes Streichholz weniger gibt als u,
            # Wird das umzulegende Streichholz auf den ehemaligen Platz des passenden gelegt
            Lösung += f"\n{umzulegendesStreichholz} wird an diese Positionen verschoben und gedreht {passendesStreichholz}."
        elif u >= umzulegend + 2:
            # Wenn es noch weniger umzulegende Streichhölzer gibt,
            # werden die fehlenden miteinander getauscht
            Lösung += f"\n{u - umzulegend} andere Streichhölzer tauschen gegenseitig ihre Plätze."
        # Der Lösungssatz Lösung wird zurückgegeben
        return Lösung

    # Jedes Streichholz von Nachher wird um den Vektor verschoben
    # UmzulegendNachher speichert umzulegende Streichhölzer von Nachher
    # UmzulegendVorher speichert umzulegende Streichhölzer von Vorher
    UmzulegendNachher = {
        k: [vektorMinus(i, Vektor) for i in v] for (k, v) in Nachher.items()
    }
    UmzulegendVorher = {0: [], 30: [], 60: [], 90: [], 120: [], 150: []}
    # Mit umzulegend werden die umzulegenden Streichhölzer gezählt,
    umzulegend = 0
    for Winkel in Vorher:
        for Vorherpunkt in Vorher[Winkel]:
            if Vorherpunkt in UmzulegendNachher[Winkel]:
                # Wenn ein Streichholz passend ist, wird es aus UmzulegendNachher gelöscht,
                # damit am Ende die umzulegenden Streichhölzer übrig bleiben
                UmzulegendNachher[Winkel].remove(Vorherpunkt)
                # passendesStreichholz ist ein passendes Streichholz von Vorher
                passendesStreichholz = [Vorherpunkt, Winkel]
            else:
                # Wenn nicht, wird UmzulegendVorher das Streichholz hinzugefügt
                UmzulegendVorher[Winkel] += [Vorherpunkt]
                umzulegend += 1
                # umzulegendesStreichholz ist ein umzulegendesStreichholz von Vorher
                umzulegendesStreichholz = [Vorherpunkt, Winkel]
        if umzulegend > u:
            # Falls es mehr umzulegende Streichhölzer gibt als u, wird die Funktion abgebrochen
            return None
    # Wenn genau u Streichhölzer umgelegt werden müssen, wird die Lösung zurückgegeben
    return ausgeben(UmzulegendVorher, UmzulegendNachher)


def streichholzrätsel():
    if u == n:
        # Wenn u und n gleich sind, wird jeder Vektor eine Lösung zurückgeben
        return übereinanderlegen([0, 0, 0, 0])
    # Vektoren speichert alle Vektoren
    Vektoren = []
    # Alle Vektoren, bei denen es mindestens 1 umzulegendes Streichholz gibt, werden erstellt
    for Winkel in Vorher:
        for Vorherpunkt in Vorher[Winkel]:
            for Nachherpunkt in Nachher[Winkel]:
                Vektor = vektorMinus(Nachherpunkt, Vorherpunkt)
                # Wenn der Vektor noch nicht getestet wurde,
                # bestimmt die Vergleichsfunktion, ob der Vektor der richtige Vektor ist
                if Vektor not in Vektoren:
                    Vektoren += [Vektor]
                    Ergebnis = übereinanderlegen(Vektor)
                    if Ergebnis:
                        # Wenn eine Lösung gefunden wurde, wird diese zurückgegeben
                        return Ergebnis
    # Wenn keine Lösung gefunden wurde, ist das Rätsel nicht lösbar
    return "Das Rätsel ist nicht lösbar"


print(streichholzrätsel())