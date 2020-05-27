### Parcial II Fund. Prog.
### FUnciones en Python (programación estructurada)
### Nicolás Rendón Arias, Manuel Alejandro Bermúdez, Oscar Julián Toro

#============================ Inicio parcial ====================================
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
#============(A)==============

import random   #importa la librería random
import numpy as np   #importa librería numpy como np

#============(listas para sub_punto C)==============
listaDatos=[]   #declara lista de datos
restar=[]   #declara lista para la resta
elevar=[]   #declara lista para elevar
#============()=====================================
#========= (Lista para punto_fibonacci) ============
lisFib=[]
#============()=====================================
#========= (Lista para punto_4.1) ==================
lista = []   #define la lista para punto 4.1
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

'''
2)
En matemáticas, la sucesión o serie de Fibonacci es la siguiente sucesión infinita
de números naturales:
Desarrolle una funcion que pida una posición e imprima la serie gibonacci hasta ese
termino.
'''

#==================== Inicio sucesión de Fibonacci =======================

def fib_i(n):   #define la función para fib
    a, b = 0, 1   # variables a y b toman valores de 0 y 1
    while n > 0:   #mientras n sea mayor a 0...
        a, b = b, a + b   #opera con sumas la sucesion en a y b
        n -= 1   # n va disminuyendo
    return a   #devuelve a

def func_LlamadaFib():
    num=int(input(" Ingrese el numero final de la sucesion: "))   #pide el límite de la sucesion
    for i in range(num):   # para i en el rango del número digitado...
        lisFib.append(fib_i(i))   #lo guarda en la lista de resultados...
    return lisFib   #retorna la lista

#==================== Fin sucesión de Fibonacci =======================

'''
2.1)
Pida un término para K y Calcule el valor de la sumatoria
'''

# =================== Inicio serie geométrica alternada =======================

k=int(input('Deme un término para K: '))   #pide el valor para K...

def func_serGeom(k):   #define la función de la sucesión...
    conRep=100   #establece contador de repeticiones...
    acuSum=0   #declara un acumulador para la suma
    for x in range (conRep):   #para X en el rango del contador de repeticiones...
        term=((math.pow(-1,k))*(math.pow(2/3,k-1)))   #opera la fórmula de la sumatoria
        acuSum=acuSum+term   #el resultado se va guardando en el acumulado
        k=k+1  #la variable K va incrementando con el ciclo...


    return acuSum   # devuelve el acumulado

resultFnal=func_serGeom(k)   #variable con llamado a la función como parámetro K


# =================== Fin serie geométrica alternada =======================

'''
3)
Pida un término para K y Calcule el valor de la sumatoria
'''
# =================== Inicio serie p alternada =======================

k=int(input('Deme un término para K: '))   #pide el valor de K al usuario...

def func_serAlt(k):   #define la función para serie p alternada
    conRep=100   #establece contador de repeticiones
    acuSum=0   #declara un acumulador de suma
    for x in range (conRep):   #para X en el rango del contador de repeticiones...
        ter=((math.pow(-1,k-1))*(1/(math.pow(k,1/3))))   #opera la fórmula de la sumatoria...
        acuSum=acuSum+ter   #adiciona el resultado al acumulado...
        k=k+1   #incremento de la variable K con el ciclo

    return acuSum   #devuelve el acumulado

resultFnal=func_serAlt(k)   #establece variable con llamado a la función y parámetro K


# =================== Fin serie p alternada =======================

'''
4)
Genera una lista de 10 posiciones con datos aleatorios y desarrolle las funciones que:
• Sume los elementos del vector
• Calcule la suma de los pares y de impares
• Calcule la suma de los elementos de las posiciones impares
• Que pida una posición y que inserte un valor en dicha posición
• Ordene el vector
• Con el vector ordenado que lea un numero por teclado y lo inserte en la posición correcta
'''

# ============(4)================

for conCic in range(10):   #para el contador del ciclo en el rango de 10...
    lista.append(random.randrange(1, 20))   #la lista recibe un valor aleatorio entre 1 y 20

print(lista)   #imprime la lista

# ============(4.1)==============
def func_suma(lista):   #define la función de suma
    suma = 0    #variable para acumulado de suma
    for conCic in range(len(lista)):   #para el contador de ciclo en el rango de la longitud de la lista...
        suma = suma + lista[conCic]    #el elemento en posición del contador se añade al acumulado
    print("La suma de todos los valores de la lista es: ", suma)   #imprime un aviso y la suma




# ============(4.2)==============
def func_sumaParImpar(lista):   #define función para pares e impares
    sumapar = 0   #variable para suma de pares
    sumaimpar = 0   #variable para suma de impares
    for conCic in range(len(lista)):   #para el contador de ciclo en el rango de la longitud de la lista...
        if lista[conCic] % 2 == 0:   #si el residuo de la división/2 del elemento actual es igual a cero...
            sumapar = sumapar + lista[conCic]   #lo añade al acumulado de suma pares
        else:   #sino...
            sumaimpar = sumaimpar + lista[conCic]   #lo añade al acumulado de suma impares
    print("La suma de los valores pares es: ", sumapar)   #imprime la suma pares
    print("La suma de los valores impares es: ", sumaimpar)   #imprime la suma impares




# ============(4.3)==============
def func_sumaPosImpar(lista):   #define función para suma de pos impares
    sumapos = 0   #variable para acumulado de suma
    for conCic in range(len(lista)):   #para el contador del ciclo en el rango de la longitud de la lista...
        if lista.index(lista[conCic]) % 2 != 0:   #con el index devuelve la pos del elemento en cuestión...
            #si el residuo de su división/2 es diferente de cero...
            sumapos = sumapos + lista[lista.index(lista[conCic])]   #lo añade al acumulado
    print("la suma de las posiciones impares de la lista es: ", sumapos)   #imprime el acumulado




# ============(4.4)==============
def func_insertar(lista):   #define la funcion insertar
    valor = int(input("Ingrese la posicion: "))   #se le pide un valor al usuario...
    nuevovalor = int(input("Ingrese el valor a insertar: "))   #se pide un valor nuevo a insertar...
    lista[valor] = nuevovalor   #se hace el intercambio
    print(lista)   #imprime el vector modificado




# ============(4.5)==============
def func_ordenarlista(lista):   #define función para ordenar lista
    for conCic in range(len(lista) - 1, 0, -1):   #para el contador del ciclo en el rango de 1-0- longitud list...
        for i in range(conCic):   #para i en el rango del contador...
            if lista[i] > lista[i + 1]:   #si el elemento actual es mayor al que le sigue...
                temp = lista[i]   #guarda el valor del actual en variable temporal...
                lista[i] = lista[i + 1]   #valor actual toma el valor del que le sigue
                lista[i + 1] = temp   #el valor en pos i+1  toma el valor del temporal
    print(lista)   #imprime lista ordenada




# ============(4.6)==============
def func_insertordenada(lista):   #define funcion para insertar en pos correcta...
    valor = int(input("Ingrese un valor: "))   #se pide al user el ingreso del valor
    lista.append(valor)   #la lista recibe al valor
    for conCic in range(len(lista) - 1, 0, -1):   #para el contador del ciclo en el rango de 1-0- longitud list...
        for i in range(conCic):   #para i en el rango del contador...
            if lista[i] > lista[i + 1]:   #si el elemento actual es mayor al que le sigue...
                temp = lista[i]   #guarda el valor del actual en variable temporal...
                lista[i] = lista[i + 1]   #valor actual toma el valor del que le sigue
                lista[i + 1] = temp   #el valor en pos i+1  toma el valor del temporal
    print(lista)   #imprime lista modificada ordenada

#================ (Bloque de llamados a funciones) ======================
#================ (Bloque de impresion de avisos) =======================

#======================== (Llamados punto_1) ============================

print('Matriz_1')
print(A)
print('Matriz_2')
print(B)

print('La suma de los elementos: ', func_SumElemMat(A))   #imprime aviso y resultado

print('Matriz ordenada')   #imprime aviso
print(func_OrdMat(A))   #llamado a la funcion

print('La media de los elem. es: ', func_MedMat())   #imprime aviso + llamado a la func

main()  #llamado a la función

print('La mediana de la matriz: ', str(func_MedianaMat(func_OrdMat(A))))   #se imprime aviso y resultado

print('Mayor valor de la matriz: ', str(func_MayValMat(func_OrdMat(A))))   #imprime aviso y resultado

print('Menor valor de la matriz: ', str(func_MenValMat(func_OrdMat(A))))   #imprime aviso y resultado

print('Suma de las dos matrices: ', func_SumEleDosMat())   #imprime aviso y llamado a la funcion

print('Multiplicacion de las matrices:')   #imprime un aviso
print(func_MultMat())   #imprime el llamado a la func.


#================================= () ===================================

#======================== (Llamados punto_2.0) ==========================

print(func_LlamadaFib())   #llamado a la función

#================================= () ===================================

#======================== (Llamados punto_2.1) ==========================

print('La serie geométrica de ', k, 'es: ')   #imprime un aviso...
print(round(resultFnal,3))   #imprime el resultado y lo redondea a 3 decimales.

#================================= () ===================================

#======================== (Llamados punto_3) ============================

print('La serie P alternada de:  ', k, 'es: ')   #imprime un aviso
print(round(resultFnal,3))   #imprime el resultado y lo redondea con 3 decimales.

#================================= () ===================================

#======================== (Llamados punto_4) ============================

func_suma(lista)   #llamado a la función 4.1

func_sumaParImpar(lista)   #llamado a la función 4.2

func_sumaPosImpar(lista)   #llamado a la función 4.3

func_insertar(lista)   #llamado a la función 4.4

func_ordenarlista(lista)   #llamado a la función con la lista como parámetro 4.5

func_insertordenada(lista)  #llamado a la función con lista como parámetro...  4.6

#================================= () ===================================

#================ (Fin Bloque de llamados a funciones) ======================
#================ (Fin Bloque de impresion de avisos) =======================

#============================ Fin parcial ====================================
#============================== (V1.2) =======================================