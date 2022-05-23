##def fibnochi(n):
##    a,b=0,1
##    print(a,b,end=' ')
##    for i in range(2,n+1):
##        c=a+b
##        print(c,end=' ')
##        a,b=b,c
##n=int(input())
##fibnochi(n)


##def near_fib(n):
##    a,b=0,1
##    c=a+b
##    while c<=n:
##        c=a+b
##        a,b=b,c
##    if n-a>b-n:
##        print(b)
##    elif n-a<b-n:
##        print(a)
##    else:
##        print(a,b,end=" ")
##n=int(input())
##near_fib(n)

def near_fib(n):
    a,b=0,1
    c=a+b        ##i=2
    while c<=n:
        c=a+b
        a,b=b,c
        if b>n:
            print(a)
            break
        ##i+=1
n=int(input())
near_fib(n)



