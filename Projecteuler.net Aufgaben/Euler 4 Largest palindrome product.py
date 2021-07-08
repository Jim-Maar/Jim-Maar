global awnser
awnser = 0

def multiplicator(n):
    m = n-1
    while awnser == 0:
        n = n-1
        m = 999
        while m >= n:
            check_palindrome(n,m)
            m = m-1
    print("awnser = ",awnser)
    return

def check_palindrome(n,m):
    x = n*m
    s = str(x)
    is_palindrome = True
    for e in range(0,len(s)):
        if s[e] != s[e*-1 -1]:
            is_palindrome = False
            break;
    if is_palindrome == True:
        awnser = x
        print(n," * ",m," = ",awnser)
    return

multiplicator(1000)
