abundantnums = []
for i in range(1,281):
    summ = 0
    for ii in range(2,int(i**0.5)+1):
        if i % ii == 0 and ii != i/ii:
            summ += ii + i/ii
    if summ+1 > i:
        abundantnums += [i]
#print(abundantnums)

summnums = []

for i in range(0,len(abundantnums)):
    for ii in range(i,len(abundantnums)):
        if abundantnums[i] + abundantnums[ii] > 28123:
            break
        #if abundantnums[i] + abundantnums[ii] not in summnums:
        summnums += [abundantnums[i] + abundantnums[ii]]

summnums.sort()
print(summnums)
for i in range(0,len(summnums)):
    if i == 0:
        summ = sum(list(range(1,summnums[i])))
        #print(list(range(1,summnums[i])), sum(list(range(1,summnums[i]))))
    else:
        summ += sum(list(range(summnums[i-1]+1,summnums[i])))
        #print(list(range(summnums[i-1]+1,summnums[i])), sum(list(range(summnums[i-1]+1,summnums[i]))))
        #print(summ)
    
print(summ)
