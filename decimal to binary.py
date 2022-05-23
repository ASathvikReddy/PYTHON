def decbin(n):
    s=''
    while n>0:
        r=n%2
        s+=str(r)
        n//=2
    return s[::-1]
n=int(input())
print('binary of n is =',decbin(n))
