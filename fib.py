import sys

n1 = 1
n2 = 1
count  = 3
print(1)
print(1)
while count <= int(sys.argv[1]):
	n1 = n1+n2
	n2 = n1+n2
	print (n1)
	count +=1

	print(n2)
	count +=1


