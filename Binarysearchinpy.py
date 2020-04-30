def Binarysearch(arr,lo,hi,x):
	while lo<=hi:
		mid=(lo+(hi))//2

		if arr[mid]==x:
			return mid

		if arr[mid]<x:
			lo=mid+1

		if arr[mid]>x:
			hi=mid-1
	return -1


arr=[2,3,4,10,40]
x=10
result=Binarysearch(arr,0,len(arr)-1,x)

  
if result != -1: 
    print ("Element is present at index %d" % result) 
else: 
    print ("Element is not present in array")