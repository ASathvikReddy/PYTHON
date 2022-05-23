def bindec(n):
    i=0
    r=0
    while n:
        rem=n%10
        r=r+rem*(2**i)
        n//=10
        i+=1
    return r
n=int(input())
print('decimal of',n,'is =',bindec(n))


 
