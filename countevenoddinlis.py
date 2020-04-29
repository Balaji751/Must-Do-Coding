lis=[1,2,3,4,5]
ecount=0
ocount=0
for i in lis:
	if i%2==0:
		ecount+=1
	if i%2!=0:
		ocount+=1
print(ecount,ocount)