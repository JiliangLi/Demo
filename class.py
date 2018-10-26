# for a dog

# properties:
#	stamina/energy
#	name
#	height/weight
#	appearance
#	happiness

# methods:
#	bark
#	eat
#	sleep
#	play
#	poop


class Dog:			# class starts with a capital letter and the term should be singular
	# constructor
	def __init__(self, energy, name):
		self.energy = energy
		self.hunger = 5
		self.weight = 30
		self.happiness = 5
		self.name = name

	# methods - functions
	def eat(self):
		status = ""
		if self.hunger > 0:
			self.weight += 1
			self.hunger -= 1
			self.energy += 1
			self.happiness += 1
			status = self.name + " just ate."
			if self.weight > 40:
				self.happiness -= 3
				status += "\nFYI, this dog is unhappy because it's getting fat."
		else:
			status = "Nope, not eating. Not hungry."
		return status

	def stats(self):
		return "Name: " + self.name + "\nHunger: " + str(self.hunger) + "\nEnergy: " + str(self.energy) + "\nHappiness: " + str(self.happiness) + "\nWeight: " + str(self.weight)

class Height:
	def __init__(self):
		self.height = 0
		self.food = 0
		self.sleep = 0
	def eat(self):
		growth = "Delicious."
		if self.height < 10:
			self.height += 1
			growth += "\nI just grew."
		else:
			growth += "\nBut I have reached my maximum height."
		return growth
	def nap(self):
		growth = "Just got some sleep."
		if self.height < 10:
			self.height += 1
			growth += "\nI just grew."
		else:
			growth += "\nBut I have reached my maximum height."
		return growth

myHeight = Height()
print(myHeight.eat())
print(myHeight.nap())
print(myHeight.eat())
print(myHeight.nap())
print(myHeight.eat())
print(myHeight.nap())
print(myHeight.eat())
print(myHeight.nap())
print(myHeight.eat())
print(myHeight.nap())
print(myHeight.eat())
print(myHeight.nap())
print(myHeight.eat())
print(myHeight.nap())
print(myHeight.eat())
print(myHeight.nap())



# myDog = Dog(3, "Tim")
# mySecondDog = Dog(8, "Annabelle")
# print(myDog.stats())
# print(myDog.eat())
# print(myDog.eat())
# print(myDog.eat())
# print(myDog.eat())
# print(myDog.eat())
# print(myDog.eat())
# print(myDog.stats())



