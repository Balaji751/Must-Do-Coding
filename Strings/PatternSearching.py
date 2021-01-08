def pattren(s,d):
    e=len(d)
    l=[]
    count=0
    for i in range(len(s)):
        st=s[i:i+e]
        if st==d:
            count+=1
            l.append(i)
    print(*l)
    return 



a=input().split()
s=a[0]
d=a[1]
print(pattren(s,d))