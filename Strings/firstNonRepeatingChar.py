def fnrc(a):
    l=[]
    for i in range(len(a)):
        b=a.count(a[i])
        if b>=2:
            continue
        else:
            l.append(a[i])
    if len(l)==0:
        return -1
    else:
        return l[0]

a=input()
print(fnrc(a))