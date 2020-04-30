def binpal(x):
	binary=bin(x)

	# Here we are not considering 
	# first two characters because 
	# bin function appends "0b" as
	# prefix in binary representation
	binary=binary[2:]
	if binary==binary[::-1]:
		return True
	else:
		return False

x=int(input())
print(binpal(x))