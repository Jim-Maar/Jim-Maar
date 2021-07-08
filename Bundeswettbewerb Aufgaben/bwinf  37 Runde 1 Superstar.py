Menschen = {"Turing":True,
            "Hoare":True,
            "Dijkstra":True,
            "Knuth":True,
            "Codd":True}

Following = [["Turing", "Hoare"],["Turing", "Dijkstra"],["Hoare", "Turing"],["Hoare", "Dijkstra"],["Hoare", "Codd"],["Knuth", "Turing"],["Knuth", "Dijkstra"],["Codd", "Turing"],["Codd", "Dijkstra"],["Codd", "Knuth"]]
Abfragen = []
superstar = False

def follow(nameA,nameB):
    for i in Following:
        if i[0] == nameA and i[1] == nameB:
            return True
    return False

for i in Menschen:
    for ii in Menschen:
        if Menschen[i] and Menschen[ii] and i != ii:
            if follow(i,ii):
                Menschen[i] = False
            else:
                Menschen[ii] = False
            Abfragen += [[i,ii]]
            print(i,ii)

for i in Menschen:
    if Menschen[i]:
        possiblestar = i
        superstar = True

if superstar:
    for i in Menschen:
        if [possiblestar, i] not in Abfragen:
            if follow(possiblestar, i) and i != possiblestar:
                superstar = False
                break
            print(possiblestar, i)
        if [i,possiblestar] not in Abfragen and i != possiblestar:
            if not follow(i, possiblestar):
                superstar = False
                break
            print(i, possiblestar)

if superstar:
    print("der superstar ist "+ possiblestar)
else:
    print("es gibt keinen superstar")

    
