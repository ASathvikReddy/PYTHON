##a,b=map(int,input().split())
##while a!=b:
##    if a>b:
##        a=a-b
##    else:
##        b=b-a
##print(a)

def hcf(a,b):
    if a>b:
        a,b=b,a
    c=a
    while 1:
        if a%c==0 and b%c==0:
            return c
        c-=1
a,b=map(int,input().split())
print(hcf(a,b))
