import random

guessesTaken=0
print("Hello, What is your name?")
name=input()
number=random.randint(1,20)
print("Well,"+name+",I'm thinking of a number between 1 to 20")

while guessesTaken<6:
	print('Take a guess')
	guess=input()
	guess=int(guess)

	guessesTaken+=1

	if(guess<number):
		print('Number guess is too low')

	if(guess>number):
		print("Number guess is too high")

	if(guess==number):
		break
if(guess==number):
	guessesTaken = str(guessesTaken)
	print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')

if(guess!=number):
	number = str(number)
	print('Nope. The number I was thinking of was ' + number)
	