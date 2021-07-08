import math
triangle_num = 1
adder = 2
devider = 0
while devider <= 50:
    devider = 0
    for i in range(1,math.ceil(math.sqrt(triangle_num+1))):
        if triangle_num % i == 0:
            if i == math.sqrt(triangle_num):
                devider = devider+1
            else:
                devider = devider +2
            #print("triangle_num=",triangle_num,"teilbar durch",i,"devider=",devider)
    triangle_num = triangle_num + adder
    adder = adder +1
print(triangle_num-(adder-1))
            
