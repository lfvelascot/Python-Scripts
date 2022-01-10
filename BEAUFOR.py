cadena1 = "LUISFÉLIPEVELASCOTAO"
clave = "CIGÜEÑACIGÜEÑACIGÜEÑ"
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÄËÏÖÜ"
i = 0
crip = ""
while i < 20:
	x = abecedario.find(cadena1[i])
	y = abecedario.find(clave[i])
	r = (x-y)%37
	print ("X = ",x," Y = ",y," R = ",r)
	crip = crip+abecedario[r]
	x = 0
	y = 0 
	r = 0
	i+=1

print(crip)
