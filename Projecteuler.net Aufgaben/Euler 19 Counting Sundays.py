Months = [31,28,31,30,31,30,31,31,30,31,30,31]

count = 0
d = 2
def counting_sundays():
    global x
    global d
    global count
    for j in range(1901,2001):
        for m in Months:
            if d % 7 == 0:
                count += 1
            if ((j % 4 == 0 and j % 100 != 0)or j % 400 == 0)and m == 28:
                d = d + 29
            else:
                d = d + m
    return(count)

print(counting_sundays())
