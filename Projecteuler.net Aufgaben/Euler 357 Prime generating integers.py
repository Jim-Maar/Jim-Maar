import math

primes = []
#nonprimes = []

def isPrime(m):
    #else:
        #if m in nonprimes:
            #print(m)
            #return False
    if m == 1:
        return False
    if m in primes:
        return True
    else:
        for t in range(2,math.ceil(math.sqrt(m+1))):
            if m % t == 0:
                #nonprimes.append(m)
                return False
        primes.append(m)
        return True

nums = []
num= 30
while len(nums) <= num-1:
    nums.append(True)

for d in range(1,math.ceil(math.sqrt(len(nums)+1))):
    for n in range(d,len(nums)+1,d):
        if nums[n-1] == True and d <= math.sqrt(n):
            if isPrime(d + n/d) == False:
                nums[n-1] = False

count = 0
for i in range(0,len(nums)):
    if nums[i] == True:
        #print(i+1)
        count = count + i+1

print(nums)
print(count)
                
        
        

    
    
