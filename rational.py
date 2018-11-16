''' 
	inspired by: 
	http://anandology.com/python-practice-book/object_oriented_programming.html
	
	other resources:
	https://docs.python.org/3/reference/datamodel.html
	https://docs.python.org/3/library/operator.html
'''

from fractions import Fraction

class RationalNumber:
	def __init__(self, n, d):
		self.n = n
		self.d = d

	def __add__(self, other):
		n = self.n*other.d + self.d*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __sub__(self, other):
		n = self.n*other.d - self.d*other.n
		d = self.d*other.d		
		return RationalNumber(n, d)

	def __mul__(self, other):
		n = self.n*other.n
		d = self.d*other.d
		return RationalNumber(n, d)

	def __truediv__(self, other):
		# if not isinstance(other, RationalNumber):
	 #   		other = RationalNumber(other)
		n = self.n*other.d
		d = self.d*other.n	
		return RationalNumber(n, d)


	# complete this first!
	def __str__(self):
		# if self.d % self.d

		# return  self.n/self.d
		return "%s/%s" % (self.n, self.d)
		# return  str(Fraction(self.n/self.d))

	__repr__ = __str__ # what does this do?



def main():
	a = RationalNumber(1, 2)
	b = RationalNumber(1, 3)
	print(a-b)
	print(a+b)
	# print(a) # 1/2
	# print(b) # 1/3
	print(a+b) # 5/6
	print(a-b) # 1/6
	print(a*b) # 1/6
	print(a/b) # 3/2


main()