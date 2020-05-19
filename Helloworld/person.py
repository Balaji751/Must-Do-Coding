class Person:
	def __init__(self,name):
		self.name=name

	def talk(self):
		print("Hi I'm"+" "+self.name)

person=Person("Balu")
print(person.name)
person.talk()