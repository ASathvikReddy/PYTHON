def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True

a,b=map(int,input().split())
c=0
for i in range(a,b+1):
    if prime(i) and prime(i+2):
        c+=1
print(c)
