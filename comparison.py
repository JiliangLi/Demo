#x = 5
#y = x + 3
#z = y*2 - x

#print (z+y>=8)


#x = 5
#a = x == 6
#print (not a)

x=7
y=3
z=2

a = x>y
b = x<y
c = z+y>=x-z

print ((a and c) or b)
print (a or not b)
print ((b and a) and (c or b))
print (not (b and(c and(a or b))))