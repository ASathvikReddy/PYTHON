
##def fibno_recur(n):
##    if n==0:
##        return 0
##    elif n==1:
##        return 1
##    else:
##        return fibno_recur(n-1)+fibno_recur(n-2)
##n=int(input())
##print(fibno_recur(n))

##
##def fibno_recur(n):
##    if n==1 or n==2:
##        return 1
##    else:
##        return fibno_recur(n-1)+fibno_recur(n-2)




def fibno_recur(n):
    if n<=1:
        return n
    return fibno_recur(n-1)+fibno_recur(n-2)

n=int(input())
for i in range(n):
    print(fibno_recur(i),end=' ')








