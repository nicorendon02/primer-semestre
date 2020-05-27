#============(A)==============

import random   #importa la librería random
import numpy as np   #importa librería numpy como np

#============(listas para sub_punto C)==============
listaDatos=[]   #declara lista de datos
restar=[]   #declara lista para la resta
elevar=[]   #declara lista para elevar
#============()=====================================

#============(Primera matriz)==============
A = np.random.randint(100, size=(5,5))   #genera 1ra matriz 5x5 con valores aleatorios hasta el 100
#============()============================
B = np.random.randint(100, size=(5,5))   #genera 2da matriz 5x5 con valores aleatorios hasta el 100


def func_SumElemMat(mat):   #define función para suma elem. de matriz...
    sumElem = mat.sum()    #operación para sumar los elementos

    return sumElem   #retorna valor



#============(Fin A)==============
#============(B)==============

def func_OrdMat(mat):   #define func para ordenar la matriz
    matOrdLis = np.sort(mat, None)   #convierte la matriz a vector y ordena
    matOrd = np.array(matOrdLis).reshape(5, 5)   #vuelve a organizar como 5x5 la matriz

    return matOrd   #retorna la matriz aleatoria ordenada





def func_MedMat():   #define func para media de la matriz
    medMat = (func_SumElemMat(A))/25   #operacion para la media de la matriz
    return medMat    #retorna el resultado


#============(Fin B)==============
#============(C)==============

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



#============(Fin C)==============
#============(D)==============

def func_MedianaMat(matriz):   #define func para mediana de la matriz
    medianaMat = matriz[2,2]   #se declara variable con la pos de la mediana

    return medianaMat   #retorna el resultado


#============(Fin D)==============
#============(E)==============

#Mayor valor de la matriz
def func_MayValMat(matr):   #define func para mayor valor de la matriz
    valMayMat = matr[4,4]   #declara variable con pos del mayor valor de la matriz

    return valMayMat    #retorna el resultado

#============(Fin E)==============
#============(F)==============

#Menor valor de la matriz
def func_MenValMat(matrz):   #define func para menor valor de la matriz
    valMenMat = matrz[0,0]   #declara variable con pos del menor elemento de la matriz

    return valMenMat   #retorna el resultado

#============(Fin F)==============
#============(G)==============
#Suma elem matrices...

def func_SumEleDosMat():   #define func para suma elementos matrices
    sum1=A.sum()   #define suma para matriz A
    sum2=B.sum()   #define suma para matriz B
    sumTot=sum1+sum2   #define suma total

    return sumTot   #retorna el resultado



#============(Fin G)==============
#============(H)==============
#multip. elem matrices...

def func_MultMat():   #define func para multip. de las matrices...
    resMult = np.dot(A, B)   #usa la funcion dot() para multiplicar matrices A y B

    return resMult   #retorna el resultado...


#============(Fin  H)==============
#============(Fin punto_1)==============