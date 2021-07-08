import math
import time

start = time.time()

finished = {}

def sumofdivisers(n):
    if n in finished:
        return finished[n]
    summ = 1
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            summ += i + n/i
    finished[n] = summ
    return summ
summ = 0


for n in range(1,10001):
    b = sumofdivisers(n)
    if n == sumofdivisers(b) and n != b:
        summ += n

end = time.time()

print(end-start)
print(summ)
    
