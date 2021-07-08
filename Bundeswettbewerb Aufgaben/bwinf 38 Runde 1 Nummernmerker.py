Number = "011000000011000100111111101011"
Anfänge = [0]
Blöcke = []
for i in range(0,len(Number)):
    if Number[i] == "0" and i >= 3 and Number[i-1] != "0":
        Anfänge += [i-1]
        
print(Anfänge)
Anfänge += [len(Number)]
print(Anfänge)

#for i in range(0,len(Anfänge)-1):
i = 0
while i <len(Anfänge)-1:
    while Anfänge[i+1]- Anfänge[i] >= 6:
        Anfänge.insert(i+1,Anfänge[i]+4)
        i = 0
    else:
        if Anfänge[i+1]- Anfänge[i] == 5:
            Anfänge.insert(i+1,Anfänge[i]+3)
            if i+1 == len(Anfänge)-1:
                Anfänge
            i = 0
    i += 1
        
print(Anfänge)

for i in range(0,len(Anfänge)-1):
    Blöcke += [Number[Anfänge[i]:Anfänge[i+1]]]
    
print(Blöcke)
    
        
        
