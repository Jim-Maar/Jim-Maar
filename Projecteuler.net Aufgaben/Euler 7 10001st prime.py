'''
numbers = []
for i in range(1,10002):
    numbers.append(i)

for i in numbers:
    for x in numbers:
        if x % i == 0 and x != i and i != 1:
            numbers.remove(x)
print(numbers)
'''
import math
n = []
x = 1
while len(n) < 10001:
    x = x+1
    teilbar = False
    for i in range(2,round(math.sqrt(x))+1):
        if x % i == 0 and x != i:
            teilbar = True
            break;
    if teilbar == False:
        n.append(x)
print(x)
