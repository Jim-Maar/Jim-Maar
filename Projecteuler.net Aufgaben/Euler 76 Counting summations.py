n = [6]

while n[0] > 1:
    i = -1
    while n[i] == 1:
        i = i -1
    n[i] -= 1
    #print(n[0])

    l = -1
    i2= i
    while l > i:
        del n[-1]
        #print(n)
        l -= 1
        i += 1
    #print(n[0])
    while sum(n) < 6:
        if 5 - sum(n) > n[i]:
            n.append(n[i])
        else:
            n.append(6 - sum(n))
    print(n)
