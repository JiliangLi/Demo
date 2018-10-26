#celsius = float(input ("Please enter degrees in celsius:"))
#kelvin = celsius + 273.15
#print ("The temperature is:",kelvin)

#Fahrenheit = float (input ("Please enter degrees in Fahrenheit:"))
#Celsius = (Fahrenheit - 32) * 5 / 9
#print ("The termperature in Celsius is "+str(Celsius))

import random as r
import math as m


θ = r.random ()*m.pi*1

y = m.sin(θ)**2+m.cos(θ)**2
print (y)