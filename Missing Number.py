for i in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    print(((a*(a+1))//2-sum(b)))



Input:                    
2                                        
4                                        
1 4 3                           
5
2 5 3 1
Output:
2
4


Explanation:
For first test case
Vaibhav placed 4 integers but he picked up only 3 numbers. So missing number will be 2 as it will become 1,2,3,4.

For the second case
Vaibhav placed 5 integers on the board, but picked up only 4 integers, so the missing number will be 4 so that it will become 1,2,3,4,5.