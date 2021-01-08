from itertools import permutations
def lexci(a):
    l=[]
    b=sorted(a)
    c=permutations(b)
    for i in c:
        l.append(''.join(i))
    for i in range(len(l)):
        if l[i]==a:
            return i+1


a=input()
print(lexci(a))