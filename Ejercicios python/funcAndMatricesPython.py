# TALLER FUNCIONES Y MATRICES
#===============================================================================
# 1)
import math
import random
arregloA=[]
for x in range(1,31):
    num=int(random.randrange(100))
    arregloA.append(num)
    print("elemento "+ str(x)+ " es: "+ str(num))
print("=====================================================================")
print(arregloA)
print("================================================================================")
def sumaPromLista(listaNumeros):
    cic=0
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
        prom=laSuma/len(listaNumeros)
        promNum=round(prom,2)
        print("la suma " + str(cic+1) + " es: " + str(laSuma))
        cic=cic+1
    print("el promedio es: "+ str(promNum))
print(sumaPromLista(arregloA))
print("==========================================================================")
def numMayMen(listaNum):
    numMay=max(listaNum)
    numMen=min(listaNum)
    print("el elemento mayor de la lista es: "+ str(numMay))
    print("el elemento menor de la lista es: "+ str(numMen))
numMayMen(arregloA)

#===============================================================================
# 2)
import math
import random
arregloA=[]
for x in range(1,31):
    num=int(random.randrange(100))
    arregloA.append(num)
    arregloA.sort()
    print("elemento "+ str(x)+ " es: "+ str(num))
print("=====================================================================")
print(arregloA)
print("================================================================================")
def func_numParImpar(listaNum):
    arregloI=[]
    arregloP=[]
    for i in listaNum:
        if i%2!=0:
            arregloI.append(i)
        else:
            arregloP.append(i)
    print("lista de elementos pares: "+ str(arregloP))
    print("lista de elementos impares: "+ str(arregloI))
func_numParImpar(arregloA)

#===============================================================================
# 3)
import random

lisVal = []

def fun_OrdenList():
    for x in range(30):
        val = random.randrange(1, 20)
        lisVal.append(val)
    print('Lista aleatoria: ' + str(lisVal))

    temp = 0
    for x in range(1, len(lisVal)):
        for y in range(0, len(lisVal) - x):
            if lisVal[y] > lisVal[y + 1]:
                temp = lisVal[y + 1]
                lisVal[y + 1] = lisVal[y]
                lisVal[y] = temp
    print('Lista ordenada: ' + str(lisVal))
    lisVal.reverse()
    print('Lista ordenada de mayor a menor: ' + str(lisVal))

fun_OrdenList()

#===============================================================================
# 4)
import random
arregloA=[]
arregloB=[]
for x in range(1,31):
    numA=int(random.randrange(30))
    numB=int(random.randrange(30))
    arregloA.append(numA)
    arregloB.append(numB)
print("=====================================================================")
print("arreglo A:  "+ str(arregloA))
print("================================================================================")
print("arreglo B: "+ str(arregloB))
print("=====================================================================")
def fun_potNum(listaA,listaB):
    arregloC=[]
    for x in range(30):
        numElev=listaA[x]**listaB[x]
        arregloC.append(numElev)
        print(str(listaA[x])+" a la "+ str(listaB[x])+ " es: "+ str(numElev))
    print("============================LISTAS:============================================")
    print("=====================================================================")
    print("arreglo A:  "+ str(arregloA))
    print("================================================================================")
    print("arreglo B: "+ str(arregloB))
    print("====================================================================")
    print("arreglo C: "+ str(arregloC))
fun_potNum(arregloA,arregloB)

#===============================================================================
# 5)
import random
arregloA=[]
arregloB=[]
for x in range(1,31):
    numA=int(random.randrange(100))
    numB=int(random.randrange(100))
    arregloA.append(numA)
    arregloB.append(numB)
print("=====================================================================")
print("arreglo A:  "+ str(arregloA))
print("================================================================================")
print("arreglo B: "+ str(arregloB))
print("=====================================================================")
def fun_sumaNum(listaA,listaB):
    arregloC=[]
    for x in range(30):
        numSum=listaA[x]+listaB[x]
        arregloC.append(numSum)
        print(str(listaA[x])+" + "+ str(listaB[x])+ " es: "+ str(numSum))
    print("============================LISTAS:===================================================")
    print("=======================================================================================")
    print("arreglo A:  "+ str(arregloA))
    print("=======================================================================================")
    print("arreglo B: "+ str(arregloB))
    print("=========================================================================================")
    print("arreglo C: "+ str(arregloC))
fun_sumaNum(arregloA,arregloB)

#===============================================================================
# 6)
import math
import random
arregloA=[]
for x in range(1,31):
    numA=int(random.randrange(100))
    arregloA.append(numA)
print("=====================================================================")
print("arreglo A:  "+ str(arregloA))
print("================================================================================")
def fun_numRep(listaNumeros):
    for x in range(len(listaNumeros)):
        rep=listaNumeros.count(listaNumeros[x])
        print(str(listaNumeros[x])+ " se repite: "+ str(rep)+ " vez/veces")
fun_numRep(arregloA)

#===============================================================================
# 7)
import math
import random
arregloA=[]
arregloB=[]
for x in range(11):
    numA=int(random.randrange(5))
    numB=int(random.randrange(5))
    arregloA.append(numA)
    arregloB.append(numB)
print("=====================================================================")
print("arreglo A:  "+ str(arregloA))
print("================================================================================")
print("arreglo B: "+ str(arregloB))
print("=====================================================================")
def fun_numRep(listaA,listaB):
    for x in range(len(listaA)):
        repA=listaA.count(listaA[x])
        print(str(listaA[x])+ " de la lista A,se repite: "+ str(repA)+ " vez/veces")
        print("=================================================================================")
    for y in range (len(listaB)):
        repB=listaB.count(listaB[y])
        print(str(listaB[y])+ " de la lista B,se repite: "+ str(repB)+ " vez/veces")
        print("=======================================================================================================")
fun_numRep(arregloA,arregloB)

#===============================================================================
# 8)
texto=input("Ingrese una cadena de texto: ")
def func_cadenatxt(texto):
    numcarac=len(texto)
    for conCic in range (len(texto)):
        if texto[conCic]==" ":
            numcarac=numcarac-1
    print("El numero de caracteres es: ",numcarac)
func_cadenatxt(texto)

#===============================================================================
# 9)
    texto = input("Ingrese una cadena de texto: ")
    tex = texto.casefold()

    def func_cadenatxt(texto):
        a = 0
        e = 0
        i = 0
        o = 0
        u = 0
        for conCic in range(len(texto)):
            if texto[conCic] == "a":
                a = a + 1
            elif texto[conCic] == "e":
                e = e + 1
            elif texto[conCic] == "i":
                i = i + 1
            elif texto[conCic] == "o":
                o = o + 1
            elif texto[conCic] == "u":
                u = u + 1
            repA = texto.count("a")
            repE = texto.count("e")
            repI = texto.count("i")
            repO = texto.count("o")
            repU = texto.count("u")

        print("la letra A se repite: " + str(repA) + " vez/veces")
        print("la letra E se repite: " + str(repE) + " vez/veces")
        print("la letra I se repite: " + str(repI) + " vez/veces")
        print("la letra O se repite: " + str(repO) + " vez/veces")
        print("la letra U se repite: " + str(repU) + " vez/veces")

    func_cadenatxt(tex)

#===============================================================================
# 10)
from random import choice
longitud=int(input("ingrese la longitud que quiere para su password  "))
def fun_pasword(longitud):
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
    password = ""
    password = password.join([choice(valores) for i in range(longitud)])
    print("su password es: "+ str(password))
fun_pasword(longitud)

#===============================================================================
# 11)
password = input("ingrese la contraseña ")


def fun_clave(password):
    validar = False  # que se vayan cumpliendo los requisitos uno a uno.
    long = len(password)  # Calcula la longitud de la contraseña
    espacio = False  # variable para identificar espacios
    mayuscula = False  # variable para identificar letras mayúsculas
    minuscula = False  # variable para contar identificar letras minúsculas
    numeros = False  # variable para identificar números
    y = password.isalnum()  # si es alfanumérica retona True
    correcto = True  # verifica que hayan mayuscula, minuscula, numeros y no alfanuméricos

    for carac in password:  # ciclo for que recorre caracter por caracter en la contraseña

        if carac.isspace() == True:  # Saber si el caracter es un espacio
            espacio = True  # si encuentra un espacio se cambia el valor user

        if carac.isupper() == True:  # saber si hay mayuscula
            mayuscula = True  # acumulador o contador de mayusculas

        if carac.islower() == True:  # saber si hay minúsculas
            minuscula = True  # acumulador o contador de minúsculas

        if carac.isdigit() == True:  # saber si hay números
            numeros = True  # acumulador o contador de numeros

    if espacio == True:  # hay espacios en blanco
        print("La contraseña no puede contener espacios")
    else:
        validar = True  # se cumple el primer requisito que no hayan espacios

    if long < 8 and validar == True:
        print("seguridad baja, Mínimo 8 caracteres")
        validar = False  # cambia a Flase si no se cumple el requisito móinimo de caracteres
    elif long > 8 and validar == True:
        print("invalido, Maximo 8 caracteres")
        validar = False  # cambia a Flase si no se cumple el requisito maximo de caracteres
    if mayuscula == True and minuscula == True and numeros == True and y == False and validar == True:
        validar = True  # Cumple el requisito de tener mayuscula, minuscula, numeros y no alfanuméricos
    else:
        correcto = False  # uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple

    if validar == True and correcto == False:
        print(
            "La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")

    if validar == True and correcto == True:
        print("La contraseña  es altamente segura")


fun_clave(password)

#===============================================================================
# 12)
from numpy import *
import numpy as np
import random
matriz =[]
numero_filas=int(input("ingrese el numero de filas "))
numero_columnas=int(input("ingrese el numero de columnas "))
def func_valran():
    for conCic in range(25):
        valor=random.randrange(20)
        return valor
for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(func_valran())
print(matriz)

#===============================================================================
# 13-14)
from numpy import *
import numpy as np
import random
matriz =[]
numero_filas=int(input("ingrese el numero de filas "))
numero_columnas=int(input("ingrese el numero de columnas "))
def func_valran():
    for conCic in range(25):
        valor=random.randrange(20)
        return valor
for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(func_valran())
print(array(matriz))
print("La suma de todos los elementos de la matriz es : ",(np.sum(matriz)))
print("El promedio de todos los elemenos de la matriz es: ",(np.sum(matriz))/(numero_filas*numero_columnas))

#===============================================================================
# 15)
from numpy import *
import numpy as np
import random

matriz = []
numero_filas = int(input("ingrese el numero de filas "))
numero_columnas = int(input("ingrese el numero de columnas "))


def func_valran():
    for conCic in range(25):
        valor = random.randrange(20)
        return valor


for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(func_valran())
print(array(matriz))
listsumfil = []
listsumcol = []
for filas in range(numero_filas):
    sumfilas = np.sum(matriz[filas])
    listsumfil.append(sumfilas)

for columnas in range(numero_columnas):
    sumcol = np.sum([fila[columnas] for fila in matriz])
    listsumcol.append(sumcol)

print("la suma de las filas es: ", array(listsumfil))
print("la suma de las columnas es: ", listsumcol)

#===============================================================================
# 16)
from numpy import *
import numpy as np
import random
matriz =[]
numero_filas=int(input("ingrese el numero de filas "))
numero_columnas=int(input("ingrese el numero de columnas "))
def func_valran():
    for conCic in range(25):
        valor=random.randrange(20)
        return valor
for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(func_valran())
matrizOrd=np.asarray(matriz)
print("MATRIZ ORDENADA")
print(matrizOrd)
print('Diagonal (sum): ', np.trace(matrizOrd))
print('Diagonal (elements): ', np.diagonal(matrizOrd))
matrizVol=np.fliplr(matrizOrd)
print("MATRIZ VOLTEADA")
print(matrizVol)
print('diagonal  secundaria(sum): ', np.trace(matrizVol))
print('diagonal secundaria (elementos): ', np.diagonal(matrizVol))

#===============================================================================
# 17-18)
from numpy import *
import numpy as np
import random

matriz1 = []
matriz2 = []
matrizsum = []
numero_filas = int(input("ingrese el numero de filas para la primer matriz "))
numero_columnas = int(input("ingrese el numero de columnas para la primer matriz "))


def func_valran():
    for conCic in range(25):
        valor = random.randrange(20)
        return valor


for i in range(numero_filas):
    matriz1.append([])
    matrizsum.append([])
    for j in range(numero_columnas):
        matriz1[i].append(func_valran())
        matrizsum[i].append(0)

for m in range(numero_filas):
    matriz2.append([])
    for n in range(numero_columnas):
        matriz2[m].append(func_valran())
print(array(matriz1))
print("")
print(array(matriz2))

for conI in range(numero_filas):
    for conJ in range(numero_columnas):
        matrizsum[conI][conJ] = (matriz1[conI][conJ] + matriz2[conI][conJ])

print("La suma de las matrices es: ")
print(array(matrizsum))

#===============================================================================
# 19)
from numpy import *
import numpy as np
import random

matriz1 = []
matriz2 = []
numero_filas1 = int(input("ingrese el numero de filas para la primer matriz "))
numero_columnas1 = int(input("ingrese el numero de columnas para la primer matriz "))


def func_valran():
    for conCic in range(25):
        valor = random.randrange(20)
        return valor


for i in range(numero_filas1):
    matriz1.append([])
    for j in range(numero_columnas1):
        matriz1[i].append(func_valran())

numero_filas2 = int(input("ingrese el numero de filas para la segunda matriz "))
numero_columnas2 = int(input("ingrese el numero de columnas para la segunda matriz "))
for m in range(numero_filas2):
    matriz2.append([])
    for n in range(numero_columnas2):
        matriz2[m].append(func_valran())
print(array(matriz1))
print("")
print(array(matriz2))

print("La multiplicacion de las 2 matrices es: ")
print(np.dot(matriz1, matriz2))

#===============================================================================
# 20)
from numpy import *
import numpy as np
import random
import pandas

matriz = []
numero_filas = int(input("ingrese el numero de filas "))
numero_columnas = int(input("ingrese el numero de columnas "))


def func_valran():
    for conCic in range(25):
        valor = random.randrange(20)
        return valor


for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(func_valran())
matrizOrd = np.asarray(matriz)
print("MATRIZ ORDENADA")
print(matrizOrd)
mt = pandas.DataFrame(matriz)
print("INGRESE 1 SI DESEA  UNA FILA Y 2 SI DESEA  UNA COLUMNA")
elecc = int(input("ingrese numero: "))
if elecc == 1:
    fil = int(input("ingrese la fila que desea : "))
    for nroF in range(numero_filas + 1):
        if fil == nroF:
            sumaFila = np.sum(matrizOrd[nroF])
            promFiLa=sumaFila/(nroF+1)
            print("la suma de la fila " + str(nroF) + " es: " + str(sumaFila))
            print("el promedio de la fila " + str(nroF) + " es: " + str(promFiLa))

elif elecc == 2:
    columna = int(input("ingrese la columna que desea modificar: "))
    for nroC in range(numero_columnas):
        if columna == nroC:
            sumaColum = mt[nroC].sum()
            promColum=sumaColum/(nroC+1)
            print("la suma de la columna "+ str(nroC)+ " es: "+ str(sumaColum))
            print("el promedio de la columna " + str(nroC) + " es: " + str(promColum))

else:
    print("esa no es una opcion")

#===============================================================================
# ©2020 Nicolás Rendón Arias, Oscar Julián Toro,Manuel Alejandro Bermúdez - V1.0
