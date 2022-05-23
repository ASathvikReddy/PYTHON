def lcm(a,b):
    c=b
    while c:
        if c%a==0 and c%b==0:
            return c
        c+=1

a=int(input())
b=int(input())
c=lcm(a,b)
print('lcm of',a,'and',b,'is',c)
