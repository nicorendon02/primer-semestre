#funcion que lea y calcule el promedio de 3 notas


def func_DatEst():
    #captura de datos
    #definicion de variables locales y captura de datos
    codEst=int(input('Digite el codigo del estudiante: '))
    nomEst=input('Digite el nombre del estudiante: '))

    #imprime los datos del estudiante
    print('Nombre: '+ nomEst)
    print('Codigo: '+ str(codEst))

#desarrollo de la funcion
def func_calDef():
    #captura de datos
    parUno=float(input('Digite el primer parcial: '))
    parDos=float(input('Digite el segundo parcial: '))
    parTres=float(input('Digite el tercer parcial: '))

    #se realizan los calculos
    notDef=(parUno+parDos+parTres)/3

    #imprime el resultado
    print('La nota definitiva es: '+str(notDef))

#llamado a la funcion
func_DatEst()
func_calDef()
