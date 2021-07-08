import time
from random import randrange
#from sympy import isprime
start = time.time()

def MillerRabin(p):
    r = 0
    if p == 2:
        return True
    if p == 1 or p % 2 == 0:
        return False
    if p == 3:
        a = 2
    else:
        a = randrange(2,p-1)
    p2 = p-1
    
    while(p2 % 2 == 0):
        p2 = p2//2
        r += 1

    x = a**p2 % p
    if x == 1 or x == p-1:
        return True

    while(r > 1):
        print(x)
        x = long(long(x*x) % p)
        if x == p-1:
            return True
        if x == 1:
            return False
        r -= 1
    return False

def is_prime(n):
    if n % 2 == 0 and n != 2 or n % 3 == 0 and n != 3 or n == 1:
        return False
    for i in range(6,int(n**0.5)+2,6):
        if n % (i-1) == 0 or n % (i+1) == 0:
            return False
    return True

def quersumme(a):
    s=0
    while a!=0:
        s+=a%10
        a=a//10
    return s

fake_truncatable_Harshad_numbers = [1,2,3,4,5,6,7,8,9]
truncatable_Harshad_numbers = []
summ = 0

for t in range(1,14):
    for i in fake_truncatable_Harshad_numbers:
        quersum = quersumme(i)
        if i % quersum == 0:
            truncatable_Harshad_numbers.append(i)
            if is_prime(i / quersum) == True:
                for e in [1,3,7,9]:
                    m10pe = i*10 + e
                    if is_prime(m10pe) == True:
                        summ += m10pe
    fake_truncatable_Harshad_numbers = []
    for i in truncatable_Harshad_numbers:
        for new in range(0,10):
            fake_truncatable_Harshad_numbers.append(i*10+new)
    truncatable_Harshad_numbers = []

end = time.time()
print(end - start)
print(summ)




    
