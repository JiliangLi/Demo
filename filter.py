from PIL import Image
import colorsys

im = Image.open("Unknown.png")

x, y = im.size

image = Image.new("RGB",(x,y))


rgb_im = im.convert('RGB')


coordinate = [[(0,0,0)for i in range(y)]for j in range(x)]

for i in range(x):
	for j in range(y):
		(R, G, B) = rgb_im.getpixel((i, j))
		try:
			(H, L, S) = colorsys.rgb_to_hls(R, G, B)

		except ZeroDivisionError:
			(H, L, S) = (0, 255, 0)
		coordinate[i][j] = (H, L, S)

for i in range(x):
	for j in range(y):
		(H, L, S) = coordinate[i][j] 
		if 0 < L < 250 and (abs(S) < 0.25 or abs(H) < 0.09 or abs(H) > 1.2):

		#  or 0 < L < 75:
		# if abs(H) < 0.09 or abs(H) > 1.2:
		# if abs(H) < 0.2 or abs(H) > 0.8 or abs(S) < 0.2:
			coordinate[i][j] = (H, L-15, 0)
		else:
			coordinate[i][j] = (H-0.6, L, S)			

for i in range(x):
	for j in range(y):
		(H, L, S) = coordinate[i][j] 
		(R, G, B) = colorsys.hls_to_rgb(H, L, S)
		coordinate[i][j] = (int(R), int(G), int(B))
# print(coordinate)


for i in range(x):
	for j in range(y):
		image.putpixel((i,j), coordinate[i][j])

image.show()
image.save("filtered_image.png", "PNG")
