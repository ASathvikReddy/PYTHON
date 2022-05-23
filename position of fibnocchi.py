def near_fib(n):
    a,b=0,1
    i=3
    while 1:
        c=a+b
        a,b=b,c
        if c==n:
            print('position of n is = ',i)
            break
        i+=1
n=int(input())
near_fib(n)
