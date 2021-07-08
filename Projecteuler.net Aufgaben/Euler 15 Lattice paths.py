
moves = {}
num = 20
'''
for m in range(1,num+1):
    moves[m] = m
moves[num+1] = 0

count = 1
count2 = 1
i = num
for a in range(2,21,2):
    moves = {}
    num = a
    for m in range(1,num+1):
        moves[m] = m
    moves[num+1] = 0
    count = 1
    count2 = 1
    i = num
    #print(l)
    last = 1
    while moves[1] <= num:
            if moves[i]-moves[1] == i-1:
                if i == num:
                    print(num,moves[i],count2,count2/last)
                    last = count2
                    count2 = 0
                    
                moves[i] += 1
                count+=1
                count2 += 1
                for v in range(1,i):
                    moves[v] = v
            #print(a,moves)
            if i == 1:
                i = num
            else:
                i -= 1
print(count, moves)
'''
vercount = 3
start = 4
multis  = [2]
while vercount < num:
    if vercount >= start:
        start += 2
    a = vercount - 2
    if (a-1) % 2 == 0:
        b = 2
    else:
        b = 3

    b += num-start
    #print(vercount,num,start)
    multis.append(2+a/b)
    
    vercount += 1
multis.append(num)
#print(multis)

count = 1
count2 = 1
for o in range(1,num):
    count = int(count*multis[-1*o])
    count2 += int(count)
    
print(count2*2)
        
