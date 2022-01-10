cadena1 = "LUISTAO"
clave = "LFVT"
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def autocompletar(cadena1,clave):
	i = 0
	aux = clave
	while len(clave) <= len(cadena1):
		if i < len (clave):
			clave+= aux[i]
		else:
			i = 0
			clave+= aux[i]
		i+=1
	return clave

def vigenere (cadena1,clave,caracteres):
	if (len(clave) < len(cadena1)):
		clave = autocompletar(cadena1,clave)
	elif len(clave) > len(cadena1):
		while len(clave) <= len(cadena1):
			cadena1 += "X"
	i = 0
	crip = ""		
	while i < len(cadena1):
		crip+=abecedario[(abecedario.find(cadena1[i])+abecedario.find(clave[i]))%len(caracteres)]
		i+=1
	print(crip)

vigenere(cadena1,clave,abecedario)