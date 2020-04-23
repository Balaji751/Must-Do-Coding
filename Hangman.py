import random

name=input("What is your name?")
print("Good luck !", name)
words = ['rainbow', 'computer', 'science', 'programming',  
         'python', 'mathematics', 'player', 'condition',  
         'reverse', 'water', 'board', 'nature','coffee','Tea']
word=random.choice(words)
print("Guess the characters :")
guesses=''
turns=10
while turns>0:
 	failed=0
 	for char in words:
 		if char in guesses:
 			print(char)

 		else:
 			print("_")
 			failed+=1
 	if failed==0:
 		print("You Win")
 		print("The word is:",word)
 		break
 	guess=input("Guess a character:")
 	guesses+=guess

 	if guess not in word:
 		turns-=1
 		print("Wrong")
 		print("You have",+turns,'more guesses')

 		if turns==0:
 			print("You Loose")
 			print("The word is:",word)
 	if guess in word:
 		turns=turns
 		print("Good guess")
 		print("You have",+turns,'more guesses')
 		
 		

