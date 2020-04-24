lis1=[]
lis2=[]
for i in range(1,101):
	if i%2==0:
		lis1.append(i)
	else:
		lis2.append(i)

print("The elements in list1 are even:",lis1)
print("The elements ins list2 are odd:",lis2)