file = open("p067_triangle.txt")
file = file.readlines()
for i in range(0,len(file)):
    file[i] = file[i].replace("\n","")
    file[i] = file[i].split(" ")
    for ii in range(0,len(file[i])):
        file[i][ii] = int(file[i][ii])
#print(file)

i = -2
while i >= -1*len(file):
    for ii in range(0,len(file[i])):
        if file[i+1][ii] >= file[i+1][ii+1]:
            file[i][ii] += file[i+1][ii]
        else:
            file[i][ii] += file[i+1][ii+1]
    i -= 1
print(file[0][0])
