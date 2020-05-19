def maxsubArray(arr,size):
	max_so_far=0
	max_ending_here=0
	for i in range(0,size):
		max_ending_here+=arr[i]
		if(max_ending_here<0):
			max_ending_here=0

		elif(max_so_far<max_ending_here):
			max_so_far=max_ending_here
	return max_so_far

arr=[2,3,-1,-9,0]
size=len(arr)
res=maxsubArray(arr,size)
print(res)