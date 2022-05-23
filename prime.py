##n=int(input())
##count=0
##for i in range(2,(n//2)+1):
##    if n%i==0:
##        count+=1
##if count==0:
##    print(n,'is prime')
##else:
##    print(n,' is not prime')
##    

##n=int(input())
##
##for i in range(2,n):
##    if n%i==0:
##        print(n,'is not prime')
##        break
##else:
##    print(n,'is prime')
        
##
##n=int(input())
##for i in range(2,(n//2)+1):
##    if n%i==0:
##        print(False)
##        break
##else:
##    print(True)


def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return(False)
        
    else:
        return(True)

n=int(input())
print(prime(n))
















