import random  #importa un conjunto de datos aleatorios
#=======================LISTA1============================================================
lisX=[]                  #definimos la lista
#=========INGRESO DE VALORES==============================================================
for x in range(10):       #usamos el FOR para repetir 10 veces(10 valores)
    valor=random.randrange(100,1000)#ingresamos un valor
    lisX.append(valor)   #añadimos el valor a la lista respectiva
#=============PROCESO DE ORDENAMIENTO=====================================================
def ordenamientoBurbuja(lisX):     #definimos el tipo de ordenamiento
    for numPasada in range(len(lisX)-1,0,-1): #usamos FOR para repetir lo siguiente dependiendo del numero de elementos de la lista(en este caso 10)
        for i in range(numPasada):         #usa FOR para que se repita tantas veces como numPasada
            if lisX[i]>lisX[i+1]:      #agregamos el condicional, si un elemento x  de la lista(ej:1) es mayor que el que le sigue x+1(1+1=2, el elemento 2):
                temp = lisX[i]           #usamos la variable "temp" como un acumulador, en este caso acumula el elemento x de la lista
                lisX[i] = lisX[i+1]    #hacemos un intercambio, donde el elemento que estaba en la posicion que sigue (osea, x+1) se ubica en la posicion en la que antes estaba el elemto x
                lisX[i+1] = temp         #hacemos otro intercambio donde "temp"= elemento x, toma el lugar que dejo el elemento x+1 
#=======TODO ESTE PROCESO SE REPITE HASTA QUE LA LISTA QUEDE EN ORDEN(MENOR A MAYOR)============
ordenamientoBurbuja(lisX)
#=============FIN ORDENAMIENTO, AHORA LA IMPRESION DE LA LISTA(SALIDA)===================
print('lista sin ordenar') #imprime un aviso
print(lisX)             #imprime la lista

#============Ordenamiento burbuja con cambio de sentido==================================
def ordburbujaMayaMen(lisX):     #definimos el tipo de ordenamiento
    for numPasada in range(len(lisX)-1,0,-1): #usamos FOR para repetir lo siguiente dependiendo del numero de elementos de la lista(en este caso 10)
        for i in range(numPasada):         #usa FOR para que se repita tantas veces como numPasada
            if lisX[i]<lisX[i+1]:      #agregamos el condicional, si un elemento x  de la lista(ej:1) es mayor que el que le sigue x+1(1+1=2, el elemento 2):
                temp = lisX[i]           #usamos la variable "temp" como un acumulador, en este caso acumula el elemento x de la lista
                lisX[i] = lisX[i+1]    #hacemos un intercambio, donde el elemento que estaba en la posicion que sigue (osea, x+1) se ubica en la posicion en la que antes estaba el elemto x
                lisX[i+1] = temp         #hacemos otro intercambio donde "temp"= elemento x, toma el lugar que dejo el elemento x+1 
#=======TODO ESTE PROCESO SE REPITE HASTA QUE LA LISTA QUEDE EN ORDEN(MENOR A MAYOR)============
ordenamientoBurbuja(lisX)        
#=============FIN ORDENAMIENTO, AHORA LA IMPRESION DE LA LISTA(SALIDA)==================
print ('ordenamiento burbuja menor a mayor')    #imprime el titulo
print(lisX)                                  #imprime la lista

ordburbujaMayaMen(lisX)
#=============FIN ORDENAMIENTO, AHORA LA IMPRESION DE LA LISTA(SALIDA)==================
print ('ordenamiento burbuja mayor a menor') #imprime el titulo
print(lisX)                #imprime la lista


#================= ordenamiento con el metodo sort ====================================
print('ordenamiento utilizando el metodo sort (menor a mayor)') #imprime el titulo
lisX.sort()  #utilización de la funcion sort para ordenar
print(lisX)  #imprime la lista ordenada


#================ordenamiento con el metodo sort (reverse) ============================
print('ordenamiento utilizando el metodo sort (mayor a menor)') #imprime la lista
lisX.reverse()  #utilizacion de la funcion reverse para cambiar el sentido del ordenamiento
print(lisX)     #imprime la lista
