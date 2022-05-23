#n=int(input())
#for i in range(0,n):
 #   for j in range(0,n):
  #      if(i==0 or i==n-1 or j==0 or j==n-1):
   #         print('*',end=' ')
    #    else:
      #      print(' ',end=' ')
   # print()


n=int(input())
for i in range(1,n+1):
    for j in range(i,n):
        print('@',end=' ')
    for k in range(1,i+1):
        print('*',end=' ')
    print()
