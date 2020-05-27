#tarea funciones
print('1)')
print('DEFINICION y = x^n')

import math #importa la libreria
x=int(input('Ingrese el valor de x: ')) #pide el valor de la base
n=int(input('Ingrese el valor de n: ')) #pide el valor del exponente
result=math.pow(x,n)  #utiliza la funcion para potencia
print('y = '+str(x)+'^'+str(n)) #imprime un aviso
print('y = '+str(result)) #imprime el resultado

print('------------------------------------')
print('2)')
print('FACTORIAL DE UN NUMERO')

import math #Este módulo proporciona acceso a las funciones matemáticas definidas por el estándar

n=int(input('Ingrese el número: '))
print ("El factorial del número es: ", math.factorial(n))

#El metodo factorial() devuelve el factorial del numero en cuestión.
print('------------------------------------')
print('3)')
print('SENO Y COSENO DE UN ÁNGULO DADO EN GRADOS')

import math #importa la librería
angUno=int(input('Ingrese el valor del ángulo: ')) #recibe el valor del ángulo en grados
angDos=float(angUno) #lo convierte a flotante
angConv=math.radians(angDos) #lo convierte a radianes

#estas funciones esperan que el argumento se facilite en radianes, y no en grados

sinAngRad=math.sin(angConv) #saca el seno del angulo con la funcion
cosAngRad=math.cos(angConv) #saca el coseno del angulo con la funcion

print('El seno del ángulo es: '+str(sinAngRad)) #imprime el resultado del seno
print('El coseno del ángulo es: '+str(cosAngRad)) #imprime el resultado del coseno

print('------------------------------------')
print('4)')
print('Ejemplo 6.7 del libro-página 209.  sen(x)')

print('------------------------------------')
print('5)')
print('CONVERTIR NUMERO DECIMAL A ROMANO')

def presentacion():   #define una funcion de presentacion del programa
    print("Programa que convierte número decimal a romano")
    print("Debe ser positivo y no mayor a 3000")
    print("___________________________________")

def func_ConvNumRom():   #define una funcion con los procedimientos para recibir y convertir el numero a romano
    
    Vn=[1000,900,500,400,100,90,50,40,10,9,5,4,1] #lista con los valores numericos
    Vc=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'] #lista con caracteres

    while (True):
        x=int(input("Ingresar un número decimal / 0 terminar: ")) #pide el ingreso del numero decimal

        if (x==0): #si x es igual a 0...
            break  #rompe el ciclo

        if (x<0): #si x es menor a 0...
            print('Este número no cumple la regla') #imprime un aviso
            break #rompe el ciclo

        if (x>3000):  #si x es mayor a 3000
            print('Este número excede el límite') #imprime un aviso
            break #rompe el ciclo

        print(str(x)+':') #imprime el numero decimal
        i=0 #declara contador del ciclo

        while(x>0):  #mientras x sea mayor a 0...
            if (x>=Vn[i]):  #si x es mayor o igual al elemento actual de la lista de valores numericos...
                print(str(Vc[i])) #imprime el valor convertido a string

                x=x-Vn[i] #plantea una reducción por cada pasada
            else:   #sino...
                i=i+1  #plantea un incremento del ciclo

#llamado a las funciones    
presentacion()
func_ConvNumRom()

print('------------------------------------')
print('6)')
print('Ejemplo del libro-página 226. Área bajo la curva')



print('------------------------------------')
print('7)')
print('Ejercicios  del libro-página 243.  6.1 al 6.14')


print('---')
print('Bibliografía: Fundamentos de Programación 4ta edición - Luis Joyanes Aguilar. Capítulo6')
print('Programadores: Nicolás Rendón Arias, Oscar Julián Toro Delgado y Manuel Alejandro Bermúdez')
