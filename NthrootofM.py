import math
for i in range(int(input())):
    n,m=list(map(int,input().split()))
    a=math.pow(m,1/n)
    a_f=math.floor(a)
    a_c=math.ceil(a)
    if (math.pow(a_f,n)==m):
        print(a_f)
    elif(math.pow(a_c,n)==m):
        print(a_c)
    else:
        print(-1)



Input:
2
2 9
3 9
Output:
3
-1