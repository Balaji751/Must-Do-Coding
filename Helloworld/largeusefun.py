def find_max(lis):
	maxi=lis[0]
	for i in lis:
		if i>maxi:
			maxi=i
	print(maxi)


find_max([1,4,3,2])