name =input("Enter your name : ")
a=len(name)
if a<3:
	print("Name must be atleast 3 characters")
elif a>50:
	print("Name can be maximum of 50 characters")
else:
	print("Name looks good!")