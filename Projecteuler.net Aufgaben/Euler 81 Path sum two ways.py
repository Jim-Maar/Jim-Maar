file = open("matrix_test.txt").read().split("\n")
file = list(map(lambda x: x.split(","),file))
#file.pop()
file = list(map(lambda x: list(map(int,x)),file))
#print(file)
#"p081_matrix.txt"
#"matrix_test.txt"

dim = 5
karo = []
for x in range(0,len(file)):
    for y in range(0,len(file)):
        if len(karo) >= x+y+1:
            karo[x+y].append(file[x][y])
        else:
            karo.append([file[x][y]])

for i in range(dim,dim*2-1):
    for o in range(0,len(karo[i])):
        if karo[i-1][o] < karo[i-1][o+1]:
            print(karo[i][o],"+=",karo[i-1][o],"+",karo[i-((i-(dim-1))*2)][o])
            karo[i][o] += karo[i-1][o] + karo[i-((i-(dim-1))*2)][o]
        else:
            print(karo[i][o],"+=",karo[i-1][o+1],"+",karo[i-((i-(dim-1))*2)][o])
            karo[i][o] += karo[i-1][o+1] + karo[i-((i-(dim-1))*2)][o]
print(karo,int(karo[dim*2-2][0]))


    
