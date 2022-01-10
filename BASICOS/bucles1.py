class Mochila:

    def __init__(self, capacidad):
        self.peso = 0
        self.lista = []
        self.valor = 0
        self.capacidad = capacidad
       
    def getPeso(self):
    	return self.peso  

    def getCapacidad(self):
    	return self.capacidad 	
     
    def guardarObjeto(self,objeto):
    	self.lista.append(objeto)
    	self.peso += objeto.getPeso()
    	self.valor += objeto.getValor()

    def mostrarMochila 	(self):
    	print ("-------- M O C H I L A --------")
    	for i in self.lista:
    		i.mostrarObjeto()	
    	print("PESO MAXIMO: ",self.capacidad,
    		"\nPESO FINAL: ",self.peso,
    		"\nVALOR ALMACENADO:",self.valor)	
                              
class Objeto:

    def __init__(self,i, peso, valor):
        self.i = i
        self.peso = peso
        self.valor = valor
        self.valorporunidad = self.valor/self.peso

    def getPeso(self):
    	return self.peso  

    def getValor(self):
	    return self.valor 	

    def mostrarObjeto(self):
        print ("Objeto:",self.i," - Valor: $",self.valor," - Peso:",self.peso," gr.")         
 
def selectionsort(lista,tam):
    for i in range(0,tam-1):
        min=i
        for j in range(i+1,tam):
             if lista[min].valorporunidad > lista[j].valorporunidad:
                min=j
        aux = lista[min]
        lista[min]=lista[i]
        lista[i] = aux
    return lista    

def resultadoFinal (mochila,objetos):
	i = (len(objetos)-1) #empezamos desde el final porque están ordenados de menor a mayor
	while(mochila.getPeso() < mochila.getCapacidad() and i >= 0):
		objeto = objetos[i]
		if ((mochila.getPeso() + objeto.getPeso())  <= mochila.getCapacidad()):
			mochila.guardarObjeto(objeto)
		i-=1 
	return mochila

def llenarLista(cantidadObjetos):
	lista = []
	for i in range (cantidadObjetos):
		print ("---------- OBJETO ",i," ----------")
		peso = float(input("Peso del objeto: "))
		valor = float(input("Peso del objeto: "))
		objeto = Objeto (i,peso,valor)
		lista.append(objeto)
	return lista

def mostrarLista (mensaje,lista):
	print("-------- ",mensaje," --------")
	for i in lista:
		i.mostrarObjeto()	

print ("-------- PROBLEMA DE LA MOCHILA --------\n",
	"En este problema se plantea la necesidad de almacenar\n",
	"dentro de una mochila m elementos los cuales sean elegidos\n",
	"por su valor, y que estos no superen el peso de la mochila.\n",
	"Se le pediran los siguiente datos:\n",
	" - Peso maximo de la mochila.\n",
	" - Cantidad de objetos a evaluar (N).\n",
	" - N Objetos a evaluar.\n",
	"-------------------------------------------")
pesoMax = float (input("Peso maximo de la mochila: "))
mochila = Mochila (pesoMax)
cantidadObjetos = int (input("Cantidad de objetos a evaluar: "))
lista = llenarLista(cantidadObjetos)
mochila = resultadoFinal(mochila,selectionsort(lista, len(lista)))
mochila.mostrarMochila()
print ("-------- FIN PROGRAMA --------")

    