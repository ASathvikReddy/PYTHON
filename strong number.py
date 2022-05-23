n=int(input())
while n:
    a=int(input())
    sum=0
    temp=a
    while temp:
        r=temp%10
        temp//=10
        pro=1
        for i in range(1,r+1):
            pro*=i
        sum+=pro
    if a==sum:
        print("Strong")
    else:
        print("Not Strong")   
    n-=1
