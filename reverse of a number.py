def reverse(n):
    rev=0
    while n:
        rev=rev*10+n%10
        n//=10
    return(rev)
n=int(input())
a=reverse(n)
print(a,'is reverse of',n)
