#for x in range(1,1001):
x = 101
s = 0
s2 = 0
for i in range(1,x):
    s = s + i**2
    s2 = s2 + i
    if i == 100:
        s2 = s2**2
print(s2,"-",s,"=",s2-s)
