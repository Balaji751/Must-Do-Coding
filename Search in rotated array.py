for i in range(int(input())):
    b=int(input())
    arr=list(map(int,input().split()))
    c=int(input())
    if c in arr:
        print(arr.index(c))
    else:
        print(-1)



Input:
3
9
5 6 7 8 9 10 1 2 3
10
3
3 1 2
1
4
3 5 1 2
6

Output:
5
1
-1

Explanation:
Testcase 1: 10 is found at index 5.