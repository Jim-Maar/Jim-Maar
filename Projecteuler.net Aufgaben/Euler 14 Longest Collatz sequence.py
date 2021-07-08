from timeit import default_timer as timer
start = timer()

def count_chain(n):
    if n in chaincount:
        return(chaincount[n]);
    else:
        if n % 2 == 0:
            next_chain = count_chain(int(n/2))
            chaincount[n] = 1 + next_chain
        else:
            next_chain = count_chain((3*n +1)/2)
            chaincount[n] = 2 + next_chain
        return(chaincount[n]);

chaincount = {1:1}

record_chain = 0
for number in range(500000,1000001):
    if record_chain < count_chain(number):
        record_chain = count_chain(number)
        record = number

end = timer()
print(end - start)

print(record)
