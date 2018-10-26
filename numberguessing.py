answer = 23

def start():
	n = float(input("Please guess a number between 1 and 100: "))
	
	if n > answer:
		print("The number is too big")
		start()
	elif n < answer:
		print("The number is too small")
		start()
	else:
		print("Bingo!")

start()