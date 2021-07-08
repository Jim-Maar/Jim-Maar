import math

from timeit import default_timer as timer
start = timer()

record = 2/5

for d in range(2,1000001):
    teiler = []
    
    minN = (d//7)*3
    if d%7 > 2:
        minN = minN + 1
    if d%7 > 4:
        minN = minN + 1

    if minN / d > record and minN/d < 3/7:
        #for t in range(2, math.ceil(math.sqrt(minN))+1):
            #if minN % t == 0:
                #if d % t == 0 or (d % (minN/t) == 0 and minN/t > 1):
                    #print(minN,"/",d,t)
                    #continue;
        record = minN/d
        record_num = minN
        record_d = d
        #print(record, record_num,"/",d)

end = timer()
print(end - start)

print(record,"=",record_num,"/",record_d)

'''
    A = d
    B = minN
    while A != B:
        if A < B:
            B = B-A
        elif B < A:
            A = A-B
        elif A != 1:
            continue;

    for t in range(2, math.ceil(math.sqrt(minN))+1):
        if minN % t == 0:
            if d % t == 0 or d % (minN/t) == 0:
                continue;


    A = minN
    B = d
    m = 1
    while m*A % B != 0:
        m = m+1
    if B != m:
        continue;
            
'''
