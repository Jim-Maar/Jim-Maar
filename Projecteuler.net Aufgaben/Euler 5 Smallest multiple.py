awnser = 0
def smallest_multiple(m):
    n = 1
    while awnser == 0:
        if n % 10000000 == 0:
            print(n)
        teilbar = True
        for i in range(2, m+1):
            if n % i != 0:
                #print(n,"nicht teibar durch",i)
                teilbar = False
                break;
        if teilbar == True:
            print("awnser = ", n)
            break;
        n = n+1

smallest_multiple(20)

