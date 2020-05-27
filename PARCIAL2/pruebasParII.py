'''
1)
Genere dos matriz de tamaño 5, almacene valores aleatorios de 1 a 100 y calcule:
a. Suma de todos los elementos de la primer matriz
b. Media de la matriz
c. Desviación estándar
d. Mediana
e. Mayor valor
f. Menor valor
g. Suma las dos matrices
h. Multiplicación de las dos matrices
'''
#============(1)==============
import random   #importa la librería random
import math
import numpy as np   #importa la librería numpy con abreviación
lisVal=[]   #declara la lista 1
lisVal2=[]   #declara la lista 2

#============(A)==============
#============(Primera matriz)==============

def func_SumEleMat():   #se define la función...
    for x in range (25):   #para X en el rango de 25...
        val=random.randrange(1,100)   #valor toma un número aleatorio entre 1 y 100
        lisVal.append(val)   #la lista 1 recibe el valor

    acumSum=0   #declara un acumulador de la suma
    for x in range (len(lisVal)):   #para X en el rango de la cantidad de elementos en la lista 1...
        acumSum=acumSum+lisVal[x]   #se suma el elemento en posición X al acumulado
    return acumSum   #retorna el acumulado
    print(np.array(lisVal).reshape(5, 5))
    sum_f1 = lisVal[0] + lisVal[1] + lisVal[2] + lisVal[3] + lisVal[4]
    print('Suma de los elementos de la f1: ', sum_f1)    #MEJORAR
print('La suma es: ', func_SumEleMat())   #llamado a la función

#============(Fin A)==============

#============(B y C)==============

listaDatos=[]   #declara lista de datos
restar=[]   #declara lista para la resta
elevar=[]   #declara lista para elevar
def sumatoria(datos):  #define funcion sumatoria
        sumatoria = float(sum(datos))  #declara variable sumatoria con suma de datos como float
        return sumatoria   #devuelve sumatoria
# * Paso 2 *
def media(datos):   #define funcion 'media'
    n = len(datos)  #define variable con longitud del parámetro
    mediana = sumatoria(datos) / n  #operación para la media
    return round(mediana,2)   #devuelve el resultado con dos decilames
# * Paso 3 *
def restar_media_datos(datos):   #define función para restar media de datos

    mediana = media(datos)   #declara variable mediana
    print('Media: ', mediana)   #imprime la media

    for i in datos:   #para una variable en 'datos'...
        op = i - mediana  #opera con la mediana...
        restar.append(op)   #restar recibe a la variable

# * Paso 4 *
def elevar_cuadrado(datos):   #define funcion elevar al cuadrado

    for i in datos:   #para una variable en 'datos'...
        op = pow (i, 2)   #eleva la variable al cuadrado
        elevar.append(op)   #elevar recibe el resultado
# * Paso 6 *

def raiz_datos():   #define la funcion raiz de datos...
    desviacion = math.sqrt(media(elevar))   #le saca raiz cuadrada a la variable en parentesis...
    return round(desviacion,2)   #devuelve el resultado con dos decimales

# * Inicio *
def main():   #define funcion principal...

    repetir = int(input('Cuantos valores quieres ingresar? : '))   #pide al usuario cantidad de valores a ingresar...

    for i in range(repetir):   #para i en el rango de la cantidad de valores dada por el usuario...
            number = random.randrange(25)   #elige un valor aleatorio
            listaDatos.append(number)# agregar el valor a la lista de datos
    print(numpy.array(listaDatos).reshape(5,5))   #lo transforma a matriz con dimensiones 5x5
    suma = sumatoria(listaDatos)  #define variable suma
    print ('Sumatoria: ', suma)   #imprime la suma

    restar_media_datos(listaDatos)   #llama a la funcion

    elevar_cuadrado(restar)   #llama a la funcion

    mediana = media(elevar)   #define variable mediana
    print ('Varianza: ', mediana)   #imprime la varianza

    desviacion = raiz_datos()   #define variable desviacion
    print ('Desviación Estándar: ', desviacion)   #imprime desviación estandar
    print ('\n')   #imprime salto de línea


main()  #llamado a la función
#============(Fin B y C)==============

lisVal=[]
def func_OrdMatriz():
    aux=0   #se declara la variable auxiliar
    for x in range (1,len(lisVal)):   #para X en el rango de 1 hasta la longitud de la lista 1...
        for y in range (0,len(lisVal)-x):   #para Y en el rango de 0 hasta la longitud de la lista 1 - X...
            if lisVal[y]>lisVal[y+1]:   #si el elemento actual es mayor al que le sigue...
                aux=lisVal[y+1]   #auxiliar toma el valor del elemento que le sigue...
                lisVal[y+1]=lisVal[y]   #el elemento Y+1 toma el elemento en posición Y
                lisVal[y]=aux   #el elemento en posición Y toma el valor del auxiliar...
    medMat=lisVal[12]  #variable para la mediana de la matriz
    return lisVal   #retorna la lista 1

func_OrdMatriz()   #llamado a la función

#============(D)==============
print('La mediana es: ', lisVal[12])   #imprime la mediana
#============(E)==============
print('El mayor elemento es: ',lisVal[24])   #imprime el mayor elemento de la matriz
#============(F)==============
print('El menor elemento es: ',lisVal[0])   #imprime el menor elemento de la matriz


print(np.array(lisVal).reshape(5,5))   #convierte la lista en la matriz solicitada con datos aleatorios.

#============(Segunda matriz)==============

for x in range (25):   #para X en el rango de 25...
    val2=random.randrange(1,100)   #val2 toma un valor aleatorio entre 1 y 100
    lisVal2.append(val2)   #la lista2 recibe a val2

acumSum2=0   #variable que acumula la suma
for x in range (len(lisVal2)):   #para x en el rango de la longitud de la lista 2...
    acumSum2=acumSum2+lisVal2[x]  #se suma el elemento en posición X al acumulado
print('La suma es: ', acumSum2)   #imprime la suma

aux2=0   #se declara la variable auxiliar2
for x in range (1,len(lisVal2)):   #para X en el rango de 1 a la longitud de la lista2...
    for y in range (0,len(lisVal2)-x):   #para Y en el rango de 0 hasta longitud de lista2 - X...
        if lisVal2[y]>lisVal2[y+1]:   #si el elemento actual es mayor al que le sigue...
            aux2=lisVal2[y+1]   #la auxiliar toma el valor del elemento en posición Y+1
            lisVal2[y+1]=lisVal2[y]   #el elemento Y+1 toma el valor del actual
            lisVal2[y]=aux2   #el elemento en posición Y toma el valor del auxiliar
medMat2=lisVal2[12]   #Declara la mediana de la lista ordenada
print(lisVal2)   #imprime la lista2
print('El mayor elemento es: ',lisVal2[24])   #imprime el mayor elemento de la lista2
print('El menor elemento es: ',lisVal2[0])   #imprime el menor elemento de la lista2
print('La mediana es: ', medMat2)   #imprime la mediana de la lista2

print(np.array(lisVal2).reshape(5,5))   #convierte la lista en la matriz solicitada con datos aleatorios.

# ============(G)==============
# suma de dos matrices aleatorias

matriz1 = []   #declara lista para matriz1
matriz2 = []   #declara lista para matriz2
matrizsum = []    #declara lista para suma de las matrices
numero_filas = int(input("ingrese el numero de filas para la primer matriz "))   #pide las filas de la primera matriz
numero_columnas = int(input("ingrese el numero de columnas para la primer matriz "))   #pide las columnas de la primera matriz

def func_valran():   #define la función
    for conCic in range(25):   #para el contador del ciclo en el rango 25...
        valor = random.randrange(20)   #se asigna un valor aleatorio
        return valor   #retorna el valor


for i in range(numero_filas):   #para la variable en el rango del numero de filas...
    matriz1.append([])   #matriz1 recibe valor
    matrizsum.append([])  #matrizsuma recibe valor
    for j in range(numero_columnas):   #para j en el rango del numero de columnas...
        matriz1[i].append(func_valran())   #la matriz en posición i recibe valor...
        matrizsum[i].append(0)    #la matriz suma en posición i recibe 0

for m in range(numero_filas):   #para m en el rango del numero de filas...
    matriz2.append([])   #matriz2 recibe valor...
    for n in range(numero_columnas):   #para n en rango de las columnas...
        matriz2[m].append(func_valran())   #matriz2 en posición m recibe valor...
print(array(matriz1))   #imprime como array matriz1
print("") #imprime separador
print(array(matriz2))   #imprime como array matriz2

for conI in range(numero_filas):   # para el contador en el rango del numero de filas....
    for conJ in range(numero_columnas):   #para el contador en el rango del numero de columnas...
        matrizsum[conI][conJ] = (matriz1[conI][conJ] + matriz2[conI][conJ])   #opera la suma de las matrices

print("La suma de las matrices es: ")   #imprime el aviso...
print(array(matrizsum))   #imprime la suma de las matrices como un array

# ============(H)==============

matriz1 = []   #declara lista para matriz1
matriz2 = []   #declara lista para matriz2
numero_filas1 = int(input("ingrese el numero de filas para la primer matriz "))   #pide el ingreso de cantidad filas
numero_columnas1 = int(input("ingrese el numero de columnas para la primer matriz "))   #pide el ingreso de cantidad columnas


def func_valran():   #define la función
    for conCic in range(25):   #para el contador del ciclo en el rango de 25...
        valor = random.randrange(20)   #se obtiene un valor aleatorio...
        return valor   #devuelve el valor


for i in range(numero_filas1):   #para i en el rango del numero de filas
    matriz1.append([])   #la matriz recibe un valor...
    for j in range(numero_columnas1):   #para j en el rango del numero de columnas...
        matriz1[i].append(func_valran())   #la matriz en posición i recibe valor...

numero_filas2 = int(input("ingrese el numero de filas para la segunda matriz "))   #pide numero de filas matriz2
numero_columnas2 = int(input("ingrese el numero de columnas para la segunda matriz "))   #pide numero de columnas matriz2
for m in range(numero_filas2):   #para m en el rango del numero de filas...
    matriz2.append([])   #la matriz2 recibe valor...
    for n in range(numero_columnas2):   #para n en rango del numero de columnas...
        matriz2[m].append(func_valran())    #matriz2 recibe valor...
print(array(matriz1))   #imprime matriz1 como array
print("")  #imprime separador
print(array(matriz2))   #imprime matriz2 como array

print("La multiplicacion de las 2 matrices es: ")   #imprime un aviso...
print(np.dot(matriz1, matriz2))   #imprime la multiplicación de las matrices con apoyo de librería numpy as np