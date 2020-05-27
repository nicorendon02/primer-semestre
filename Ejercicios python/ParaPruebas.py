
print('...............................................................')
def presentacion():   #define una funcion de presentacion del programa
    print("6.1)")
    print("Media de tres números leídos del teclado")
    print("___________________________________")

def media():   #define la funcion que saca la media de tres numeros ingresados

    numUno=int(input('Ingrese el primer número: '))  #pide el primer numero
    numDos=int(input('Ingrese el segundo número: '))  #pide el segundo numero
    numTres=int(input('Ingrese el tercer número: '))  #pide el tercer numero

    medArit=(numUno+numDos+numTres)/3  #calcula la media

    print('La media es: '+str(medArit)) #imprime la media
    
#llamado a las funciones    
presentacion()
media()

print('...............................................................')
#................................................................................
import math  #importa la libreria
def presentacion():   #define una funcion de presentacion del programa
    print("6.2)")
    print("factorial de un número entero en el rango 100 a 1.000.000")
    print("___________________________________")

def factorial():  #define la funcion factorial
    x=int(input('Ingrese un valor: ')) #pide un valor

    if x>=100 and x<=1000000:  #si el valor es mayor o igual a 100 y menor o igual a 1000000...
        print('El factorial de ',x,' es: ',math.factorial(x))  #imprime el factorial
    else:  #sino...
        print('El número no cumple la condición')  #imprime un aviso

#llamado a las funciones
presentacion()
factorial()

print('...............................................................')
#................................................................................

def presentacion():   #define una funcion de presentacion del programa
    print("6.3)")
    print("Máximo común divisor de cuatro números")
    print("___________________________________")

def mcd(a, b):
    """ Esta función calcula el MCD (Máximo Común Divisor)
        de dos números utilizando el algoritmo de Euclides.
    """
    r = a % b if b != 0 else a
    return b if r == 0 else mcd(b, r)
 
 
def f(numbers):
    if len(numbers) >= 2:
        r = mcd(numbers[0], numbers[1])
        for n in numbers[2:]:
            r = mcd(r, n)
        return r
 
numbers = []
i = 1
# Solicito los números
# En esta caso solicito 4 números

while i <= 4:
    try:
        num = int(input("Ingresa el número {}: ".format(i)))
        numbers.append(num)
        i += 1
    except ValueError as e:
        print("El valor ingresado no es un entero valido")
 
# Llamo a la función
presentacion()
result = f(numbers)
print('El MCD es: ',result)

print('...............................................................')
#................................................................................

def presentacion():   #define una funcion de presentacion del programa
    print("6.4)")
    print("el mayor de dos números enteros")
    print("___________________________________")

def maximo_numero():
    
    num1=input('ingrese primer numero: ')
    num2=input('ingrese segundo numero: ')
 
 
    if num1<num2:
        print('el mayor numero entre', num1, 'y', num2, 'es ', num2)
 
 
    elif num1>num2:
        print('el mayor numero entre', num1, 'y', num2, 'es ', num1)

    else:
        print('Son iguales')

#llamado a las funciones
presentacion()
maximo_numero()

print('...............................................................')
#................................................................................

def presentacion():   #define una funcion de presentacion del programa
    print("6.6)")
    print("dd/mm/aa")
    print("___________________________________")

def func_fecha():   #se define la funcion
    dia=int(input("Ingrese el dia: "))
    mes=int(input("Ingrese el mes: "))
    año=int(input("Ingrese el año: "))
    print(dia,"/",mes,"/",str(año)[-2:]) #el [-2:] muestra los ultimos dos numeros del año

#llamado a las funciones
presentacion()
func_fecha()

print('...............................................................')
#................................................................................

def presentacion():   #define una funcion de presentacion del programa
    print("6.7)")
    print("conversión de coordenadas polares (r, θ) a coordenadas cartesianas (x, y)")
    print("___________________________________")

import math  #importa la libreria
def func_coordPolCarte():  #define la funcion
    hipo=int(input("ingrese la medida de r (lado largo, en entero)"))
    ang=int(input("ingrese el angulo"))
    angDos=float(ang) #lo convierte a flotante
    angConv=math.radians(angDos)
    sinAngRad=math.sin(angConv) #saca el seno del angulo con la funcion
    cosAngRad=math.cos(angConv) #saca el coseno del angulo con la funcion
    cordX=hipo*cosAngRad
    cordY=hipo*sinAngRad
    cordXCart=round(cordX,2) #muestra solo dos decimales
    cordYCart=round(cordY,2)

    print("las coordenadas cartesianas son: "+ str(cordXCart)+" (X), y" + str(cordYCart)+"(Y)")

#llamado a las funciones
func_coordPolCarte()
presentacion()

print('...............................................................')
#................................................................................

def presentacion():   #define una funcion de presentacion del programa
    print("6.8)")
    print("función salario")
    print("___________________________________")

def func_salario():
    horas=int(input("Ingrese la cantidad de horas trabajadas semanalmente: "))
    salhoras=int(input("Ingrese el salario por hora: "))
    
    if horas>40:
        hrsextra=(horas-40)
        salhrsextra=(salhoras*1.5)
        print(salhrsextra)
        salario=(40*salhoras)+(hrsextra*salhrsextra)
        print("El salario del trabajador es: ",salario)
    else:
        salario=(horas*salhoras)
        print("El salario del trabajador es: ",salario)
        
#llamado a las funciones
presentacion()
func_salario()

print('...............................................................')
#................................................................................

def presentacion():   #define una funcion de presentacion del programa
    print("6.9)")
    print("función booleana Digito que determine si un carácter es uno de los dígitos 0 al 9")
    print("___________________________________")

def func_Dig():
    num=float(input("ingrese un numero:  "))
    if num>0 and num<9:
        print("True")
    else:
        print("False")

#llamado a las funciones
presentacion()
func_Dig()

print('...............................................................')
#................................................................................

def presentacion():   #define una funcion de presentacion del programa
    print("6.10)")
    print("valor absoluto de un número")
    print("___________________________________")

import math
def func_abs():
    num=int(input('Ingrese un número: '))
    print('El valor absoluto de ',num,' es: ',math.fabs(num))

#llamado a las funciones
presentacion()
func_abs()

print('...............................................................')
#................................................................................

def presentacion():   #define una funcion de presentacion del programa
    print("6.11)")
    print("División y residuo con sumas y restas")
    print("___________________________________")

def func_DiviResto():
    print("================================================================================")
    dividendo=int(input("ingrese el dividendo:  "))
    print("================================================================================")
    divisor=int(input("ingrese el divisor:  "))
    print("================================================================================")
    resultado=dividendo//divisor
    divisorSum=0
    for x in range(resultado):
        divisorSum=divisorSum+divisor
        print("la suma "+ str(x+1)+": "+ str (divisorSum))
        print("===============================================================================")
        resto=(dividendo-divisorSum)
    print("el cociente es:  "+ str(x+1))
    print("================================================================================")
    print("el resto es:  "+ str(resto))
func_DiviResto()

presentacion()
print('...............................................................')
#................................................................................

def presentacion():   #define una funcion de presentacion del programa
    print("6.12)")
    print("Fecha válida")
    print("___________________________________")

def func_val_fecha():
    
    dia=int(input('Ingrese el día: '))
    mes=int(input('Ingrese el mes: '))
    año=int(input('Ingrese el año: '))

    print(dia,'/',mes,'/',str(año)[-2:])

    if dia<1 and dia>30:
        print('Fecha invalida')

    elif dia>29 and mes==2:
        print('Fecha invalida')

    elif mes<1 and mes>12:
        print('Fecha invalida')

    elif año<1:
        print('Fecha invalida')

    else:
        print('Fecha valida')

func_val_fecha()
presentacion()
print('...............................................................')

