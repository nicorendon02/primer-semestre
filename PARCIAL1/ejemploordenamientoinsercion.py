#======LISTA CON VALORES ALEATORIOS=============
import random
lisVal=[]
for m in range(3):
    val=random.randrange(10,50)
    lisVal.append(val)
print('VISTA PREVIA',lisVal)
#===============================================
#========INICIO DEL ORDENAMIENTO================
for x in range(1,len(lisVal)):
    valor=lisVal[x] #valor toma el dato actual (funciona como temporal)
    i=x-1   #variable 'i' toma el dato de la variable del for - 1
    while i>=0:  #mientras la variable sea mayor o igual a cero...
        if valor<lisVal[i]:  #si dato actual es menor al anterior...
            lisVal[i+1]=lisVal[i] #intercambio
            lisVal[i]=valor  #el dato anterior pasa a la posicion del actual
            i=i-1  #va reduciendo de a uno
        else:  #sino...
            break   #rompe el ciclo
print('LISTA ORDENADA',lisVal)
#==========FIN DEL ORDENAMIENTO=================
#el ordenamiento por insercion compara el valor actual con el anterior
