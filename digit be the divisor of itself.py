n=int(input())
while n:
    a=int(input())
    c=0
    temp=a
    while temp:
        r=temp%10
        if r!=0 and a%r==0:
            c+=1
        temp//=10
    n-=1
    print(c)
            
