
import math   #importa la libreria
 
def factorial(x):   #define la funcion para el factorial
    factorial=1
    while x>1:      
        factorial*=x
        x-=1    # x=x-1
    return factorial
 
def seno(x):         #define la funcion para el sen(x)
    repeticiones=99.0   #declara repeticiones del ciclo
    suma=1.0            
    n=0.0
    seno=0.0
    decimales=4        #declara cantidad de decimales para el resultado
    while(n<repeticiones):   #mientras la variable sea menor a las repeticiones...
        n+=1      # n=n+1   contador del ciclo
        numerador=float((-1)**n)*(x**(2*n+1))
        denominador=float(factorial(2.0*n+1.0))
        suma=float(numerador/denominador)
        if n%2!=0:
            seno+=suma
        else:
            seno-=suma
    senofinal=seno+x    #resultado final es igual al seno + el ángulo en radianes
    senofinal=str(round(senofinal,decimales))   #redondea el resultado a la cantidad de decimales establecida
    return senofinal    #devuelve el resultado final
 
 
x=float(input('Dame el valor del ángulo (en radianes): '))  #pide el ángulo en radianes
 
print('Sen(',x,') es aproximadamente:',seno(x))  #imprime el resultado aproximado

    
