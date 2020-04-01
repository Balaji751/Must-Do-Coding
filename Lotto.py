from itertools import combinations
while True:
    d=list(map(int,input().split()))
    k=d.pop(0)
    if k==0:
        break
    permutation=list(combinations(d,6))
    for p in permutation:
        s=""
        for i in p:
            s+=str(i)+" "
        print(s)
    print()


In the German Lotto you have to select 6 numbers from the set {1,2,...,49}. A popular strategy to play Lotto - although it doesn’t increase your chance of winning — is to select a subset S containing k (k > 6) of these 49 numbers, and then play several games with choosing numbers only from S.

For example, for k = 8 and S = {1, 2, 3, 5, 8, 13, 21, 34} there are 28 possible games: [1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34].

Your job is to write a program that reads in the number k and the set S and then prints all possible games choosing numbers only from S.

Input Format

The input file will contain one or more test cases.

Each test case consists of one line containing several integers separated from each other by spaces.

The first integer on the line will be the number k (6 < k < 13). Then k integers, specifying the set S, will follow in ascending order.

Input will be terminated by a value of zero (0) for k.

Output Format

For each test case, print all possible games, each game on one line.

The numbers of each game have to be sorted in ascending order and separated from each other by exactly one space. The games themselves have to be sorted lexicographically, that means sorted by the lowest number first, then by the second lowest and so on, as demonstrated in the sample output below.

The test cases have to be separated from each other by exactly one blank line. Do not put a blank line after the last test case.