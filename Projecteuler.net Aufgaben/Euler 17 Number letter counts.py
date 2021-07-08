number_word1 = {1:3,
               2:3,
               3:5,
               4:4,
               5:4,
               6:3,
               7:5,
               8:5,
               9:4,
               10:3,
               11:6-3,
               12:6-3,
               13:8-5,
               15:7-4,
                18:8-5,
                0:0}

number_word2 = {1:4,
               2:6,
               3:6,
               4:5,
               5:5,
               6:5,
               7:7,
               8:6,
               9:6,
                0:0}

letter_count = 0
for i in range(1,1001):
    letter_count = 0
    n = str(i)

    letter_count = letter_count + number_word1[int(n[-1])]
    
    if len(n)>= 2:
        if n[-2] == "1" and (n[-1] == "1" or n[-1] == "2" or n[-1] == "3" or n[-1] == "5" or n[-1] == "0" or n[-1] == "8"):
            letter_count = letter_count + number_word1[int(n[-2]+n[-1])]
        else:  
            letter_count = letter_count + number_word2[int(n[-2])]
    if len(n) >= 3 and int(n[-3]) > 0:
        letter_count = letter_count + number_word1[int(n[-3])] + 7
        if int(n[-2]) == 1 or int(n[-1]) > 0:
            letter_count = letter_count + 3

    if len(n) >= 4:
        letter_count = letter_count + number_word1[int(n[-4])] + 8
    print(i,letter_count)
#print(letter_count)
