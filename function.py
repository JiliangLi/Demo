#def greetings(something):
#	print ("Hello!",something)


#greetings("Ted")
#greetings("Multiple places")
#greetings("One")
#greetings("Fred")
#greetings("Santa")
#greetings("George")

def start():
	response = input("\nGreetings! \n\nYou are looking for treasure. \nYou map says that the treasure can be found northerly. \nHowever, your friend says he heard soomeone talking about treasure in the south. \n\nDo you 1)Trust your friend, or 2) Trust the Map? ")
	if response == "1":
		friend()
	elif response == "2":
		map()
	else:
		print("\nYou must type 1 or 2. Please try again")
		wronganswer1("\nDo you 1)Trust your friend, or 2) Trust the Map? ")


def friend():
	response2 = input("To travel to the south, you would be asked to take the Choate transportation. \n\nIt will cost you 120$. \n\nAre you willing to pay for Choate transportation? 1)Yes 2)No")
	if response2 == "1":
		Choateshuttle()
	elif response2 == "2":
		noChoateshuttle()
	else:
		print("\nYou must type 1 or 2. Please try again")
		wronganswer2("\nAre you willing to pay for Choate transportation? 1)Yes 2)No ")

def map():
	print("\nYou lost. Please start over.")
	response4 = input("\nDo you wnat to play again? ")
	if response4.lower() == "yes" or response4 == "y":
		start()
	else:
		exit()

def wronganswer1(something):
	response1 = input(something)
	
	if response1 == "1":
		friend()
	elif response1 == "2":
		map()
	else:
		print("\nYou must type 1 or 2. Please try again")
		wronganswer1("\nDo you 1)Trust your friend, or 2) Trust the Map? ")

def wronganswer2(something):
	response3 = input(something)
	
	if response3 == "1":
		Choateshuttle()
	elif response3 == "2":
		noChoateshuttle()
	else:
		print("\nYou must type 1 or 2. Please try again")
		wronganswer2("\nAre you willing to pay for Choate transportation? 1)Yes 2)No ")

def Choateshuttle():
	pass

def noChoateshuttle():
	pass

start()




