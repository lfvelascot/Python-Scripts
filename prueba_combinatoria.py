#Metodo para hallar el factorial de un numero
def factorial(n):
    r=1
    for i in range(1, n+1):
        r*=i
    return r

#metodo para hallar la combinatoria
def comb(n, x):
    return factorial(n) // (factorial(x) * factorial(n - x))
    
##Probabilidad de exito, fracaso y acumulador de probabilidades
p,q,acum = (2/7),(5/7),0.0
## Numero de ensayos
n = 3
##Funcion de probabilidad aplicada en el dominio de X={0,1,2,3}
for i in range (4):
	r = comb(n,i)*(p**i)*(q**(n-i))
	acum += r 
	print("x = {}\nP(X={}) = {}C{}({})^{}({})^{} = {}\nACUM = {}".format(i,i,n,i,p,i,q,(n-i),r,acum))