##def fact(n):
##    r=1
##    for i in range(1,n+1):
##        r*=i
##    return r
##n=int(input())
##print(fact(n))



def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print(fact(n))
