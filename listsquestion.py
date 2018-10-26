# generate a random list of 6 multiples of 13 that are within 270 and does not have any number with digit 6

#solution:
import random as r

nums = []

while len(nums) < 6:
	mult = r.randrange(20)
	number = 13*mult
	digit = [x for x in str(number)]
	if "6" not in digit:
		nums += [number]

print(nums)