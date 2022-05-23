##n=int(input())
##c=0
##d=0
##p=0
##temp=n
##for i in range(2,n+1):
##    if n%i==0:
##        c+=1
##if c==1:
##    while(n):
##        d+=1
##        if n%10==2 or n%10==3 or n%10==5 or n%10==7:
##            p+=1
##        else:
##            break
##        n//=10
##if n==0 and d==p:
##    print(temp,'is mega prime')
##else:
##    print(temp,'is not a mega prime')
##    

##
##n=int(input())
##temp=n
##for i in range(2,(n//2)+1):
##    if n%i==0:
##        print("Not a prime")
##        break
##else:
##    d=0
##    p=0
##    while n:
##        r=n%10
##        n=n//10
##        d+=1
##        if r==1 or r==2 or r==3 or r==5 or r==7:
##            p+=1
####    for i in range(2,(r//2)+1):
####          if r%i==0:
####                break
####        else:
####            p+=1
##    if d==p:
##        print(temp,'is mega prime')
##    else:
##        print(temp,'is not a mega prime')

##
##def mega_prime(n):
##    for i in range(2,(n//2)+1):
##        if n%i==0:
##            break
##    else:
##        a=(n,'is a mega prime')
##        b=(n,'is not a mega prime')
##        d=0
##        p=0
##        temp=n
##        while(n):
##            r=n%10
##            n//=10
##            d+=1
##            if r==1 or r==2 or r==3 or r==5 or r==7:
##                p+=1
##        if p==d:
##            return(a)
##        else:
##            return(b)
##        
##n=int(input())
##print(mega_prime(n))

def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return(False)
    else:
        return(True)

n=int(input())
if prime(n):
    d=0
    p=0
    temp=n
    while n:
        r=n%10
        n//=10
        10
        d+=1
        if prime(r):
            p+=1
    if p==d:
        print(temp,'is a mega prime')
    else:
        print(temp,'is not a mega prime')
else:
    print("not a prime")





























