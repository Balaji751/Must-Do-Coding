def rotation(s1,s2):
    if(len(s1)!=len(s2)):
        return False
    else:
        s1=s1+s1
        e=len(s2)
        for i in range(len(s1)):
            st=s1[i:i+e]
            if st==s2:
                return True
        return False
a=input().split()
s1=a[0]
s2=a[1]
print(rotation(s1,s2))