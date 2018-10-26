# strands

from PIL import Image
import random

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx,imgy))

y = 0
x = 0

for y in range(0, 512, 8):

	color = (random.randrange(256), random.randrange(256), random.randrange(256))

	while x < 512:
		image.putpixel((y,x),(color))
		move = random.randrange(-1, 2)
		if 2 < y < 508:
			y += move
		if move == 0:
			x +=1

	x = 0




image.save("strands.png", "PNG")


