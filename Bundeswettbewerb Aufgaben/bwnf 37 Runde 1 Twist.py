import random


def twisten(wort):
    # print(wort)
    if len(wort) == 1:
        return wort
    getwisteteswort = wort[0]
    neuePositionen = list(range(1, len(wort) - 1))
    for i in range(1, len(wort) - 1):
        randompos = random.choice(neuePositionen)
        getwisteteswort += wort[randompos]
        neuePositionen.remove(randompos)
    getwisteteswort += wort[len(wort) - 1]
    return getwisteteswort


def texttwisten():
    with open("C:/Users/Jim/Desktop/bwnftwist.txt", "r") as f:
        file = f.readlines()
    text = ""
    neuertext = ""
    neueswort = ""
    for i in file:
        text += i
    for i in text:
        if (ord(i) < 65 or (ord(i) > 90 and ord(i) < 97) or ord(i) > 122) or i == " ":
            if len(neueswort) > 0:
                neuertext += twisten(neueswort)
                neueswort = ""
            neuertext += i
        else:
            neueswort += i
    return neuertext


# def textenttwisten():
