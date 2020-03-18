a=int(input())
for i in range(a):
    n,se=list(map(int,input().strip().split()))
    c=list(map(int,input().strip().split()))
    if len(c)==n:
        
        if se in c:
          print(c.index(se)+1)
        else:
          print(-1)