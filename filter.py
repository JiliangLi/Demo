# nov 16, 2018
# Eric Li
# image filter

from PIL import Image
import colorsys
import sys

def filter(name):
	im = Image.open(name)
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
			if name == "Unknown.png":
				if 0 < L < 250 and (abs(S) < 0.25 or abs(H) < 0.09 or abs(H) > 1.2):
					coordinate[i][j] = (H, L-15, 0)
				else:
					coordinate[i][j] = (H-0.6, L, S)
			else:
				if L > 165 or L < 20:
					coordinate[i][j] = (H, L, S)
				else:
					coordinate[i][j] = (H+0.6, L-40, S+0.1)



	for i in range(x):
		for j in range(y):
			(H, L, S) = coordinate[i][j] 
			(R, G, B) = colorsys.hls_to_rgb(H, L, S)
			coordinate[i][j] = (int(R), int(G), int(B))

	for i in range(x):
		for j in range(y):
			image.putpixel((i,j), coordinate[i][j])


	image.show()
	if name == "Unknown.png":
		image.save("filtered_image1.png", "PNG")
	else:
		image.save("filtered_image2.png", "PNG")


filter(sys.argv[1])
filter(sys.argv[2])