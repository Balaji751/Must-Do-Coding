lis=[1,2,3,4,5]
last=lis.pop()
first=lis.pop(0)
lis.insert(0,last)
lis.append(first)
print(lis)