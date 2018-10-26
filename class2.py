# bank account

# -- balance
# -- number of account
# interest rate 
# time
# type - checking/savings/etc.
# -- password/pin

# -- check balance
# log in/out
# -- deposit
# -- withdraw
# transfer
import random
import string

account_number_numbers = [i for i in range(10)]
random.shuffle(account_number_numbers)
account_number_letters= random.sample([j for j in list(string.ascii_lowercase)], 10)
account_number = ""

for i in range(10):
	rand = random.randrange(2)
	if rand == 0:
		account_number += str(account_number_letters[i][0])
	else:
		account_number += str(account_number_numbers[i])

class Account:			# class starts with a capital letter and the term should be singular
	# constructor
	def __init__(self):
		self.balance = 0
		self.account = account_number
		self.pin = str(277)


	# methods - functions
	def deposit(self, amount):
		status = ""
		if amount > 0:
			self.balance += amount
			status = "The account " + self.account + " now has a balance of $" + str(self.balance) +"."
		else:
			status = "Nope, not eating. Not hungry."
		return status

myAccount1 = Account()
print(myAccount1.deposit(400))

