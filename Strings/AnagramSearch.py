from itertools import permutations
def AnagramSearch(a,s,d):
    e=len(d)
    for i in range(len(s)):
        l=[]
        st=s[i:i+e]
        c=permutations(st)
        for j in c:
            l.append(''.join(j))
        print(l)
        for k in l:
            if k==d:
                return "Yes"
    return -1

a=input().split(" ")
s=a[0]
d=a[1]
print(AnagramSearch(a,s,d))