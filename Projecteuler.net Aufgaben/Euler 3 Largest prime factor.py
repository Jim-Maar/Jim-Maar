import time
import math
num = 600851475143
t = math.ceil(math.sqrt(num+1))

start_time = time.time()

while 2>1:
    if num % t == 0:
        teilbar = False
        if t % 2 == 0 or t % 3 == 0:
            teilbar = True
        else:
            for k in range(1,math.ceil(math.sqrt(t)/6)+1):
                if t % (6*k+1) == 0 or t % (6*k-1) == 0:
                    teilbar = True
                    break;
        if teilbar == False:
            print(t)
            break;
    t = t - 1

print("--- %s seconds ---" % (time.time() - start_time))
