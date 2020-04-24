
numbers=[]
x=int(input("Enter number of elements in list"))
for i in range(x):
    numbers.append(int(input()))
findNum=int(input("The number to be deleted is "))


i=0
for element in numbers:
    if(element == findNum):
        numbers.pop(i)
        x=x-1
        i=i-1
    i=i+1
    
print(numbers)