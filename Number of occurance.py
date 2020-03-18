for i in range(int(input())):
    a,b=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    count=0
    for i in range(a):
        
          if b==arr[i]:
                count+=1  
            
    if(count):
        print(count)
    else:
        print(-1)




Input:
2
7 2
1 1 2 2 2 2 3
7 4
1 1 2 2 2 2 3
Output:
4
-1

Explanation:
Testcase 1: 2 occurs 4 times in 1 1 2 2 2 2 3
Testcase 2: 4 is not present in 1 1 2 2 2 2 3

