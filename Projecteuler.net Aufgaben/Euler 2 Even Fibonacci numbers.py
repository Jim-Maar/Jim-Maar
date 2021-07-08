f1 = 0
f2 = 1
su = 0
SumOfEven = 0

while f1 + f2 <= 4000000:
    su = f1 + f2
    #print(f1," + ",f2," = ",su)
    f1 = f2
    f2 = su
    if su%2 == 0:
        SumOfEven = SumOfEven + su
print("SumOfEven = ",SumOfEven)

