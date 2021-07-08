file = open("pythonEuler18.txt")
file = file.readlines()
for n in range(0,len(file)):
    file[n] = file[n].replace("\n","")
    file[n] = file[n].split()
    for f in range(0,len(file[n])):
        file[n][f] = int(file[n][f])

cords = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
summ = 0
record = 0

for i in range(0,2**15):
    for h in range(0,14):
        if i % 2**h == 0:
            cords[h] = -1*cords[h]
        else:
            continue;
    for Wert in range(1,15):
        summ += file[Wert][int(sum(cords[0:Wert+1-1])+(Wert+1)*0.5)]
    if summ > record:
        record = summ
    summ = 0

    
print(record+file[0][0])
