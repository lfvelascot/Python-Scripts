import math
acum = 0.0
for i in range(8,11):
	r = ((7.5**i)*(math.exp(-7.5)))/(math.factorial(i))
	acum = acum + r
	print("R = "+str(r))
	print("ACUM = "+str(acum))
