def is_prime(n):
##  for i in range(2,(n//2)+1):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print(n,'is not a prime')
            break
    else:
        print(n,'is prime')
        
n=int(input())
is_prime(n)
is_prime(49)
