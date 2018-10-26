#sources: Tilden

import sys
import math as m


if len(sys.argv) == 4:
	p = float(sys.argv[1])
	r = float(sys.argv[2])
	t = float(sys.argv[3])

	a = p*(m.e**(r*t))

	print ("The final amount is:",a)

else:
	print ("Please enter three values as the command-line arguments")