import pygame
import math
from math import sin
from math import cos
from random import randint
import time

# pov ist die größe des Sichtfeldes
# speed ist die Bewegungsgeschwindigkeit
# rotspeed ist die Rotationsgeschwindigkeit
# size bzw. width und height sind die größen des Fensters in Pixeln
# Körper enthält die Punkte von allen Körpern, die dargestellt werden sollen
# Körperdreieck enthält alle Dreiecke zu jedem Körper
pov = 1
speed = 1
rotspeed = math.pi / 90
size = width, height = (400, 400)
Körper = []
KörperDreiecke = []

# In Körper und Körperdreiecke können alle möglichen Körper hinzugefügt werden
# Als Beispiel werden in diesem Programm zufällig generierte Pyramiden verwendet


# Funktion gibt eine zufällige Farbe zurück
def randomcolor():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


# Funktion gibt Addition zweier Vektoren zurück
def VektorPlus(Vektor1, Vektor2):
    return [Vektor1[i] + Vektor2[i] for i in range(0, 3)]


# Funktion gibt die Punkte einer Pyramide anhand einiger Parameter zurück
def Pyramide(Mittelpunkt, höhe, breite, länge):
    Punkte = []
    Punkte += [VektorPlus(Mittelpunkt, [0, höhe, 0])]
    Punkte += [VektorPlus(Mittelpunkt, [länge, 0, breite])]
    Punkte += [VektorPlus(Mittelpunkt, [-länge, 0, breite])]
    Punkte += [VektorPlus(Mittelpunkt, [länge, 0, -breite])]
    Punkte += [VektorPlus(Mittelpunkt, [-länge, 0, -breite])]
    Punkte += [VektorPlus(Mittelpunkt, [0, 0, 0])]
    return Punkte


# Funktion gibt die Dreiecke mit zufälligen Farben einer Pyramide zurück
def PyramidenDreiecke():
    Dreiecke = [
        [0, 1, 2, randomcolor()],
        [0, 1, 3, randomcolor()],
        [0, 4, 2, randomcolor()],
        [0, 4, 3, randomcolor()],
        [5, 1, 2, randomcolor()],
        [5, 1, 3, randomcolor()],
        [5, 4, 2, randomcolor()],
        [5, 4, 3, randomcolor()],
    ]
    return Dreiecke


# 2 Pyramiden werden mit zufälligen Positionen und Größen generiert und zu Körper und Körperdreiecke hinzugefügt
for i in range(0, 2):
    Mittelpunkt = [randint(-30, 30), randint(-30, 30), randint(-30, 30)]
    höhe, breite, länge = (
        randint(1, 40),
        randint(1, 40),
        randint(1, 40),
    )
    Körper += [Pyramide(Mittelpunkt, höhe, breite, länge)]
    KörperDreiecke += [PyramidenDreiecke()]

# Grober Ablauf
# Die Kamera befindet sich im Nullpunkt in Richtung der positiven z-Achse
# Die x-Achse geht von Links nach rechts durch den Nullpunkt
# Die y-Achse geht von Oben nach Unten durch den Nullpunkt
# Die x- und y-Achsen sind so gelegt, dass sie dem Koordinatensystem von pygame entsprechen
# Das Sichtfeld wird durch die Fäche E: z = 1 ausgemacht.
# Jeder Punkt wird auf die Fläche projeziert, indem der Schnittpunkt, der Gerade zwischen Kamera und Punkt und der Fläche bestimmt wird
# Wenn dieser innerhalb eines durch den pov definierten Bereich liegt, ist der Punkt sichtbar
# Dannach werden die Punkte angepasst, also in die Pixelkoordinaten des Fensters konvertiert
# Jeder Pixel, der ziwschen den Punkten eines Dreiecks liegt, bekommt die Farbe des Dreiecks
# Außerdem wird die Tiefe, also die z-Koordinate, jedes Pixels berechnet
# Ist ein Dreieck näher an der Kamera, werden die entsprechenden Pixel übermalt
# Das ist sehr Rechenaufwendig, so können aber auch konkave und sich schneidende Körper dargestellt werden

# Funktion passt projezierten Punkt an, also gibt Pixelkoordinaten des Fensters des Punktes zurück
def anpassen(Punkt):
    Punkt2D = [i * (width / 2 / pov) + width / 2 for i in Punkt[:2]]
    return Punkt2D


# Funktion gibt projezierten Punkt zurück
def projektion(Punkt):
    # Die x- und y-Koordinaten müssen lediglich durch z geteilt werden
    z = Punkt[2]
    Punkt = [i / z for i in Punkt]
    Punkt2D = anpassen(Punkt)
    return Punkt2D


# Funktion gibt den Schnittpunkt einer Graden zwischen Punkt1 und Punkt2 mit der Fläche E: z = 1 zurück
def projektion2(Punkt1, Punkt2):
    t = (1 - Punkt1[2]) / (Punkt2[2] - Punkt1[2])
    Punkt = [Punkt1[i] + t * (Punkt2[i] - Punkt1[i]) for i in range(0, 3)]
    return Punkt


# Funktion gibt die originelle z Koordinate eines Punktes zurück
# von dem Punkt ist nur die projezierte x- oder y-Koordinate bekannt
# und der Punkt soll auf der Gerade zwischen Punkt1O und Punkt2O liegen
def StrichZ(Punkt1O, Punkt2O, xyp, i):
    # Die Rechnung stammt aus der Gleichsetzung von der Geraden zwischen Punkt1O und Punkt2O
    # und einer Geraden die durch den Nullpunkt und die projezierte x- oder y-Koordinate geht
    # xyp ist die porjezierte x- oder y- Koordinate und i soll entweder 0 oder 1 sein, je nachdem welche es ist
    Nenner = Punkt2O[i] - Punkt1O[i] - xyp * (Punkt2O[2] - Punkt1O[2])
    if Nenner != 0:
        z = Punkt1O[2] + (
            ((xyp * Punkt1O[2] - Punkt1O[i]) * (Punkt2O[2] - Punkt1O[2])) / Nenner
        )
        return z
    return Punkt1O[2]


# Setup von Pygame
pygame.init()
screen = pygame.display.set_mode(size)
PixAr = pygame.PixelArray(screen)
pygame.display.set_caption("3D Renderer")

# lasttime ist wichtig für framerate independence
lasttime = time.time()

# alpha ist der Winkel, mit dem sich um die x-Achse gedreht wird
alpha = 0

# Die Schleife wird solange ausgeführt, bis das Fenster geschlossen wird
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # dt ist die Zeit, die seit dem letzten Frame vergangen ist multipliziert mit 60
    # Alle Variablen, die durch inputs bestimmt werden, werden mit dt multipliziert
    # so ist die Geschwindigkeit nicht abhängig von der Anzahl an Frames
    dt = time.time() - lasttime
    dt *= 60
    lasttime = time.time()

    # beta ist der Winkel, um den sich um die y-Achse gedreht wird
    beta = 0
    # moveVektor ist der Vektor um den sich bewegt wird
    # mit bewegt wird gemeint Jeder Punkt bewegt sich, sodass es so aussieht als ob sich der Betrachter bewegen würde
    # dasselbe gilt auch für die Rotation
    moveVektor = [0, 0, 0]

    # alpha, beta, pov und moveVektor werden durch die Inputs bestimmt
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        moveVektor[2] -= speed * dt

    if keys[pygame.K_s]:
        moveVektor[2] += speed * dt

    if keys[pygame.K_a]:
        moveVektor[0] += speed * dt

    if keys[pygame.K_d]:
        moveVektor[0] -= speed * dt

    if keys[pygame.K_SPACE]:
        moveVektor[1] += speed * dt

    if keys[pygame.K_LSHIFT]:
        moveVektor[1] -= speed * dt

    if keys[pygame.K_LEFT]:
        beta += rotspeed * dt

    if keys[pygame.K_RIGHT]:
        beta -= rotspeed * dt

    if keys[pygame.K_DOWN]:
        # Es soll nicht möglich sein sich mehr als 90 Grad nach oben oder unten zu schauen,
        # damit man sich nicht auf den Kopf stellen kann
        if alpha < math.pi / 2 - rotspeed * dt:
            alpha += rotspeed * dt

    if keys[pygame.K_UP]:
        if alpha > -math.pi / 2 + rotspeed * dt:
            alpha -= rotspeed * dt

    if keys[pygame.K_p]:
        # Wenn die x- und y- Koordinaten eines projezierten Punktes weniger als der pov von dem Punkt (0,0,1) entfernt sind, ist der Punkt sichtbar
        # Der pov kann auch in Grad ausgegeben werden
        pov += 0.02 * dt
        # Der pov wird ausgegeben, damit man weiß welchen Wert dieser in grad hat
        print("pov:", 2 * math.atan(pov / 2) * (180 / math.pi), "°")

    if keys[pygame.K_o]:
        pov -= 0.02 * dt
        print("pov:", 2 * math.atan(pov / 2) * (180 / math.pi), "°")

    # Körper enthält die Position von alle Punkten ohne die drehung um die xAchse
    # Körperneu wird die Position dieser Punkte um die x-Achse gedreht enthalten
    # Das wird gemacht weil die Achsen sich mitdrehen.
    # Die y-Achse soll vertikal bleiben, ansonsten wäre das so als könnte man schräg stehen (so das der Kopf nicht direkt über den Füßen sein muss)
    # Die x-Achse soll orthogonal zu der Richtung sein, in die man schaut, Sonst wäre die Steuerung praktisch an Himmelsrichtungen gebunden
    # Um diesen Effekt zu erzielen wird die Position der Punkte um die x-Achse gedreht nicht gespeichert, um die y-Achse gedreht aber schon
    Körperneu = []
    for Punkte in Körper:
        Punkteneu = []
        for Punkt in Punkte:
            Punktneu = [0, 0, 0]

            # Die Punkte werden um die y-Achse gedreht und um den BewegungsVektor bewegt
            # Dafür wird eine linerare Abbildung jedes Punktes mit der Drehmatrix um die y-Achse um den Winkel beta und eine Addition mit dem Bewegungsvektor gemacht
            Punkt[0], Punkt[1], Punkt[2] = (
                Punkt[0] * cos(beta) + Punkt[2] * sin(beta) + moveVektor[0],
                Punkt[1] * 1 + moveVektor[1],
                Punkt[0] * (-sin(beta)) + Punkt[2] * cos(beta) + moveVektor[2],
            )

            # Die Punkte in Köperneu sind die Punkte um die x-Achse gedreht
            # Dafür wird eine lineare Abbildung jedes Punktes mit der Drehmatrix um die x-Achse um den Winkel alpha gemacht
            # Alpha wird anders als beta und moveVektor nicht jeden Frame auf 0 gesetzt
            Punktneu[0], Punktneu[1], Punktneu[2] = (
                Punkt[0] * 1,
                Punkt[1] * cos(alpha) + Punkt[2] * (-sin(alpha)),
                Punkt[1] * sin(alpha) + Punkt[2] * cos(alpha),
            )
            Punkteneu += [Punktneu]
        Körperneu += [Punkteneu]

    # Der Hintergrund ist grau
    screen.fill((50, 50, 50))
    # zListe speichert die Tiefe, also die z koordinate von jedem Pixel
    # diese ist am Anfang auf 1000 gestellt. Die 3d engine hat also eine Zeichenentfernung von 1000 LE
    zliste = [[1000] * height for i in range(width)]
    for index, Punkte in enumerate(Körperneu):
        # Jedes Dreieck wird durchgegangen
        for Dreieck in KörperDreiecke[index]:
            # PunkteSichtbar enthält die Punkte vom Dreieck mit einer z-Koordinate >= 1
            # PunkteNichtSichtbar enthält die Punkte vom Dreieck mit einer z-Koordinate < 1
            # DreieckPunkte enthält die Punkte vom Dreieck auf die Fläche projeziert
            # DreieckPunkteO enthält die Punkte vom Dreieck (O steht für Original)
            PunkteSichtbar = []
            PunkteNichtSichtbar = []
            Dreieckpunkte = []
            DreieckpunkteO = []
            for i in range(0, 3):
                if Punkte[Dreieck[i]][2] >= 1:
                    PunkteSichtbar += [Punkte[Dreieck[i]]]
                else:
                    PunkteNichtSichtbar += [Punkte[Dreieck[i]]]
            # Wenn ein Punkt Sichtbar ist wird das Dreieck gezeichnet
            if len(PunkteSichtbar) >= 1:
                # Zwischen jedem Sichtbaren und nicht Sichtbaren Punkt wird der Punkt mit z = 1 bestimmt
                # Diese noch sichtbaren Punkte werden zu Dreieckpunkte und DreieckpunkteO hinzugefügt
                # So kann von einem Dreieck, dass sich teilweise hinter der Kamera befindet, der sichtbare Teil gezeichnet werden
                for Punkt1 in PunkteSichtbar:
                    for Punkt2 in PunkteNichtSichtbar:
                        Punkt2 = projektion2(Punkt1, Punkt2)
                        DreieckpunkteO += [Punkt2]
                        Dreieckpunkte += [anpassen(Punkt2)]
                # Die normalen Punkte werden in der Mitte eingeführt, damit die Benachbarten Punkte auch in der Liste nebeneinander sind
                Dreieckpunkte[1:1] = [projektion(Punkt1) for Punkt1 in PunkteSichtbar]
                DreieckpunkteO[1:1] = PunkteSichtbar

                # minX und maxX sind die minimalen/maximalen x-Werte des Dreiecks
                minX = min([int(Dreieck[0]) for Dreieck in Dreieckpunkte])
                maxX = max([int(Dreieck[0]) for Dreieck in Dreieckpunkte])
                # Listeklein enthält für jede Spalte an Pixeln ein Dictionary
                # Dort werden die äußersten y-Koordinaten mit ihrem jeweiligen z-Wert eingetragen
                listeklein = [{} for _ in range(0, int(maxX - minX) + 2)]
                # Linien enthält die Punkte zwischen denen eine Linie gezogen werden soll
                Linien = [[-1, 0], [0, 1], [1, 2]]
                # Wenn sich genau ein Punkt hinter der Fläche befindet, muss ein Viereck gezeichnet und damit eine weitere Linie gezogen werden
                if len(PunkteSichtbar) == 2:
                    Linien += [[2, 3]]
                for Linie in Linien:
                    # Punkt1 und Punkt2 sind die beiden projezierten und angepassten Punkte einer Linie
                    # Punkt1O und Punkt2O sind die beiden Punkte einer Linie
                    # xp und x2p sind die x-Koordinaten der pojezierten, aber noch nicht angepassten Punkte
                    # deltaX und deltaY sind die Differenzen der jeweiligen Koordinaten vom ersten und zweiten angepassten Punkt
                    Punkt1 = Dreieckpunkte[Linie[0]]
                    Punkt2 = Dreieckpunkte[Linie[1]]
                    Punkt1O = DreieckpunkteO[Linie[0]]
                    Punkt2O = DreieckpunkteO[Linie[1]]
                    xp = Punkt1O[0] / Punkt1O[2]
                    x2p = Punkt2O[0] / Punkt2O[2]
                    deltaX = Punkt2[0] - Punkt1[0]
                    deltaY = Punkt2[1] - Punkt1[1]
                    # signX ist das Vorzeichen von deltaX
                    if deltaX < 0:
                        signX = -1
                    else:
                        signX = 1
                    if deltaX != 0:
                        # XSteigung ist die Steigung vom projezierten x-Wert in Bezug auf den x-Wert
                        # YSteigung ist die Steigung vom y-Wert in Bezug auf den x-Wert
                        XSteigung = (x2p - xp) / deltaX
                        YSteigung = deltaY / deltaX
                        for i in range(0, int(deltaX) + signX, signX):
                            # zu jedem x-Wert wird der z-Wert berechnet
                            z = StrichZ(Punkt1O, Punkt2O, xp, 0)
                            # xp wird auf den x-Wert angepasst
                            xp += signX * XSteigung
                            # Alle koordinaten werden in listeklein eingetragen
                            x = int(Punkt1[0]) + i
                            y = Punkt1[1] + i * YSteigung
                            if 0 < x < width:
                                listeklein[x - minX][y] = z

                for x in range(minX, maxX):
                    Ydic = listeklein[x - minX]
                    if len(Ydic) > 1:
                        # minY und maxY sind der unterste bzw. oberste y-Wert in jeder Spalte
                        minY = min(Ydic)
                        maxY = max(Ydic)
                        # Punkt1O und Punkt2O sind die oberen und unteren Punkte in jeder Spalte
                        Punkt1O = [0, 0, Ydic[minY]]
                        Punkt2O = [0, 0, Ydic[maxY]]
                        # yp und y2p sind die projezierten y Werte der Punkte
                        yp = (minY - width / 2) / (width / 2 / pov)
                        y2p = (maxY - width / 2) / (width / 2 / pov)
                        # Die y-Koordinaten der Punkte werden mit yp bzw. y2p und den z-Koordinaten berechnet
                        Punkt1O[1] = yp * Punkt1O[2]
                        Punkt2O[1] = y2p * Punkt2O[2]
                        # YSteigung ist die Steigung vom projezierten y-Wert in Bezug auf den y-Wert
                        YSteigung = (y2p - yp) / (maxY - minY)
                        for y in range(
                            max(0, int(minY)) + 1, min(int(maxY) + 1, height)
                        ):
                            # Für jede x- und y-koordinate wird die z-koordinate berechnet
                            z = StrichZ(
                                Punkt1O, Punkt2O, (yp + (y - minY) * YSteigung), 1
                            )
                            # Wenn der z-Wert niederiger ist als der bisherige, werden die koordinaten in zliste eingetragen
                            # und der Pixel mit der Farbe des Dreiecks bemahlt
                            if z <= zliste[x][y]:
                                PixAr[x][y] = Dreieck[3]
                                zliste[x][y] = z
    # Das Fenster wird aktualisiert
    pygame.display.update()
# Wenn das Fenster geschlossen wird, wird pygame korrekt beendet
pygame.quit()