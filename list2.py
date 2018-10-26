# i = [[1,2,3],[4,5,6],[7,8,9]]
# print(i[2][1])

i = [0 for x in range(12)]

print(i)

j = [0]*12
print(j)

k = [[0]*10 for x in range(10)]
print(k)

for x in range(len(k)):
	print(*k[x]) #unpacking the list

