file = open("p022_names.txt")
file = file.read()
file = file.split('","')
file[0] = file[0].replace('"','')
file[-1] = file[-1].replace('"','')
file.sort()

summ2 = 0

alph = {"A": 1,
       "B": 2,
       "C": 3,
       "D": 4,
       "E": 5,
       "F": 6,
       "G": 7,
       "H": 8,
       "I": 9,
       "J": 10,
       "K": 11,
       "L": 12,
       "M": 13,
       "N": 14,
       "O": 15,
       "P": 16,
       "Q": 17,
       "R": 18,
       "S": 19,
       "T": 20,
       "U": 21,
       "V": 22,
       "W": 23,
       "X": 24,
       "Y": 25,
       "Z": 26} 

for i in range(0,len(file)):
    summ = 0
    for s in file[i]:
        summ += alph[s]
    summ = summ * (i+1)
    summ2 += summ
    #print(file[i],summ/(i+1),summ)

print(summ2)
