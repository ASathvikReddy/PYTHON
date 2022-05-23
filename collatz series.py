##def collatz(n):
##    while n!=1:
##        print(n)
##        if n%2==0:
##            n//=2
##        else:
##            n=3*n+1
##n=int(input())
##collatz(n)
##print("1")


def collatz(n):
    if n==1:
        return 1
    elif n%2==0:
        n//=2
        print(n)
    else:
        n=3*n+1
        print(n)
    return collatz(n)

n=int(input())
collatz(n)
