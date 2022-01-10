### intrucciones = 1
##Instrucciones 3n + 1


def codigo1(n):
	a  = 0 ## Asignacion variable = 1 OE
	for j in range(1,n+1):
		a+=a+j
	for k in range(n,0,-1):
		a-= 1
		a*=2
	return a


### COMPLEJIDAD
###f(x) = 3
def codigo2 ():
	x = 0 ## ASIGNACION
	x-=1
	x*=2


### f(x) = n^2 + 1
def codigo3(n):
	a=0
	for j in range(1,n+1):
		for k in range(1,n+1):
			a+= (j*k)
	return a

##COMPLEJIDAD CONSTANTE
def constante():
	salariojefecartera =6000000
	++salariojefecartera
	return salariojefecartera

def lineal (n):
	r = 0
	for i  in range (0,n):
		++r
	return r

##Busqueda dicotomica
def bus_disco (x,a,low,hight):
	 ans = -1:
	 if low == hight:
	  ans == -1
	 else:
	 	mid = ((low+(hight-low))/2)
	 	if x < a[mid] :
	 		ans = bus_disco(x,a,low,mid)
	 	elif x >a[mid]: ans = bus_disco[x,a,mid+1,hight]
	 	else: ans= mid
	 	return ans		

## CASI LINEAL

l = [15,2,5,9,1,2,10]

def quicksort(l):
	izquierda = []
	centro = []
	derecha = []
	if len(l)>1:
		pivote = l[0]
		for i in l:
			if i < pivote
				izquierda.append(i)
			elif i == pivote:
				centro.append(i)
			elif i > pivote:
			 	derecha.append(i)
			return quicksort(izquierda+ centro + quicksort(derecha)) 	
	else :
		return l

print(l)
print(quicksort(l))		

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high].getPeso()     # pivot 
    for j in range(low , high): 
        if   arr[j].getPeso() <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 