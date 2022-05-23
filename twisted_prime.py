def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return(False)

    else:
        return(True)
n=int(input())
rev=0
temp=n
if(prime(n)):    
    while(n):
        rev=rev*10+n%10
        n//=10
    if (prime(rev)):
        print (temp,'is a twisted prime')
    else:
        print(temp,'is not a twisted prime')
else:
    print('not a prime')

##
##n=int(input())
##c=0
##rev=0
##temp=n
##for i in range(2,(n//2)+1):
##    if n%i==0:
##        c=0
##        break
##else:
##    c=1
##if c==1:
##    while n:
##        rev=rev*10+n%10
##        n//=10
##for i in range(2,(rev//2)+1):
##    if rev%i==0:
##        print(False)
##        break
##else:
##    print(True)

    
