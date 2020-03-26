while True:
    try:
        
        s,t=map(str,input().split())
        a=len(s)
        b=len(t)
        if(b<a):
            print("No")
        else:
            i=0
            for j in range(b):
                if(i==a):
                    break
                if(s[i]==t[j]):
                    i+=1
            if(i==a):
                print("Yes")
            else:
                print("No")
            
    except EOFError:
        break



Input Format

The input contains several testcases. Each is specified by two strings s, t of alphanumeric ASCII characters separated by whitespace. Input is terminated by EOF.

Output Format

For each test case output, if s is a subsequence of t.

Sample Input 0

sequence subsequence
person compression
VERDI vivaVittorioEmanueleReDiItalia
caseDoesMatter CaseDoesMatter
Sample Output 0

Yes
No
Yes
No