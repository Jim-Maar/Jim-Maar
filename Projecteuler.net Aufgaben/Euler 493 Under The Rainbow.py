from random import randrange
colours = ["p","b","t","g","y","o","r"]
summ = 0
count = 0
for a in range(0,1000000):
    balls = []
    myballs = []
    
    for c in colours:
        for i in range(0,10):
            balls.append(c)

    for i in range(0,20):
        r = randrange(0,len(balls))
        b = balls.pop(r)
        if b not in myballs:
            myballs.append(b)
    summ += len(myballs)
    count += 1
    if count % 100000 == 0:
        print(summ/count)
    
