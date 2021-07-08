import math
from timeit import default_timer as timer
start = timer()

SumOfPrimes = 0
summ = 1

numbers = []
for i in range(2,2000000+1):
    numbers.append(False)

for n in range(2,math.ceil(math.sqrt(2000000+1))):
    if numbers[n-2] ==False:
        num = n
        while num <= 2000000-n:
            num = num + n
            numbers[num-2] = True

for m in range(0,len(numbers)):
    if numbers[m] == False:
        summ = summ +m+2

end = timer()
print(end-start)
print(summ)
