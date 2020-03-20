a=int(input())
for i in range(a):
    b=int(input())
    c=list(map(int,input().split(" ")))
    c.sort(reverse=True)
    # print(c)
    d=0
    for j in range(2,len(c),3):
        d+=c[j]
    print(d)
    


    
    
    
   Sample Input 0

1
6
400 100 200 350 300 250
Sample Output 0

400