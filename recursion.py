# 0! = 1	base case 
# 1! = 1	base case
# 2! = 2*1
# 3! = 3*2*1
# n! = n*(n-1)*(n-2)*...*2*1 = n*(n-1)!

# value = int(input("Number: "))

# # def factorial(n):
# # 	if n == 0 or n == 1:
# # 		return 1

# # 	return n*factorial(n-1)

# # print(factorial(value))

# def fib(n):
# 	if n == 0 or n == 1:
# 		return n

# 	return fib(n-1)+fib(n-2)


# print(fib(value))

# Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, 
# except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4. 
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

#count8(8) → 1
#count8(818) → 2
#count8(8818) → 4

value = int(input("Non-Negative Number: "))
num = 0

def count(n):
	if n == 0:
		return 0
	if n%10 == 8:
		return 1+count(n//10)
	return count(n//10)

	# if count(n) < 8:
	# 	return 0

	# elif count(n) % 10 == 8:
	# 	num += 1

	# return count(n/10)


print(count(value))








