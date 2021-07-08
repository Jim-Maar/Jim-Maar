import math
for a in range(1,math.ceil(1000/3-2)):
    for b in range(a+1,math.ceil(1000/2-1)):
        c=1000-(a+b)
        if a**2+b**2 == c**2:
            print("a=",a,"b=",b,"c=",c,"abc =",a*b*c)
        
