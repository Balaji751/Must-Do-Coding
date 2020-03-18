for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    c=1
    max=0
    for i in range(1,n):
        if arr[i]>=arr[0] and arr[i]>max:
            max=arr[i]
            c+=1
    print(c)