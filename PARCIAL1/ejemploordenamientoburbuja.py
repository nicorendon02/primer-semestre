#======LISTA CON VALORES ALEATORIOS=============
import random
lisVal=[]
for x in range(10):
    valor=random.randrange(2,10)
    lisVal.append(valor)
print('LISTA SIN ORDENAR',lisVal)
#===============================================
#========INICIO DEL ORDENAMIENTO================
temp=0  #se declara una variable temporal para evitar perdida de datos en el intercambio
for i in range(1,len(lisVal)):  #primer for
    for j in range(0,len(lisVal)-i):  #segundo for
        if lisVal[j]>lisVal[j+1]:  #si el valor actual es mayor al que le sigue...
            temp=lisVal[j+1]  #la temporal guarda el valor siguiente para que no se pierda
            lisVal[j+1]=lisVal[j]  #el valor siguiente toma el valor del actual
            lisVal[j]=temp   #el valor actual toma el valor de la temporal
print('LISTA ORDENADA',lisVal)
#==========FIN DEL ORDENAMIENTO=================
#el ordenamiento burbuja compara el valor actual con el siguiente           
           
    
