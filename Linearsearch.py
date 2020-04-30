def linearSearch(arr,x):
	for i in range(len(arr)):
		if arr[i]==x:
			return i
	return -1


arr=[10, 20, 80, 30, 60, 50,110, 100, 130, 170]
x=110
result=linearSearch(arr,x)

if result!=-1:
	print("Element is present at the index %d" % result)
else:
	print("Element is not present in array")
