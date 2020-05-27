import random        #importa valores aleatorios para la lista
#=============DEFINIR LISTA=============================
lisX=[]        #definimos la lista
#============INGRESO DE VALORES=========================
for x in range(10):           #usamos el FOR  para repetir 10 veces(10 valores)
    valor=random.randrange(100)   #escoge numeros aleatorios dependiendo del rango
    lisX.append(valor)   #añadimos el valor a la lista respectiva
#==========PROCESO DE ORDENAMIENTO======================
def ordenamientoPorInsercion(lisX):  #definimos el tipo de ordenamiento
   for indice in range(1,len(lisX)): #usamos FOR para que se repita, desde 1 hasta la cantidad de elementos de la lista.

     valorActual = lisX[indice]   #utilizamos la variable "valorActual" para almacenar un elemento x de la lista
     posicion = indice      #utilizamos la variable "posicion" para almacenar el indice 

     while posicion>0 and lisX[posicion-1]>valorActual:  #usamos un ciclo while. mientras posicion(indice) sea mayor a 0 y , el elemento anterior al elemento x (osea elemento x-1) sea mayor al valor actual(elemnto x):
         
         lisX[posicion]=lisX[posicion-1]    #hacemos un intercambio donde el elemento anterior(elemento x-1)ocupa el lugar del elemento x
         posicion = posicion-1                      #hacemos otro intercambio donde x-1 esta ahora en x

     lisX[posicion]=valorActual                 #luego un ultimo intercambio donde el valor actual(elemento x)  toma la posicion de x(que ya cambio a x-1)
#=======TODO ESTE PROCESO SE REPITE HASTA QUE LA LISTA QUEDE EN ORDEN(MENOR A MAYOR)============
ordenamientoPorInsercion(lisX)
#==========FIN ORDENMAIENTO, AHORA IMPRIMIR LA LISTA(SALIDA)================
print(lisX)    #imprime la lista
