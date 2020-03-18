a=int(input())
for i in range(a):
    n,se=list(map(int,input().strip().split()))
    c=list(map(int,input().strip().split()))
    if len(c)==n:
        
        if se in c:
          print(c.index(se)+1)
        else:
          print(-1)



 Input :
2 
5 16
9 7 2 16 4
7 98
1 22 57 47 34 18 66

Output : 
4
-1