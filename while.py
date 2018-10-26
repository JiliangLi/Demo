#num = int(input("How many times do you want to be greeted? "))

#count = 0

#while count<num:
#	print("hi!")
#	count += 1
while True:
	try:
		num = int(input("Pick a number between 1 and 5: "))
		if num >5 or num<1:
			num = int(input("That's not right. I said, pick a number between 1 and 5: "))
		else:
			print ("success!")
			break
	except ValueError:
		print("Yeah,no. That's not an integer.")
	


