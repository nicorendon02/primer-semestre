
#FUNCIONES QUE RECIBEN PARÁMETROS

#desarrollo de la funcion
def func_calPerTri(ladUno,ladDos,ladTres):  #calculo del perimetro del triangulo
    perTri=(ladUno+ladDos+ladTres)
    print('El perimetro del triangulo es: '+ str(perTri))

#llamado a la funcion
print('LLAMADO A LA FUNCION CON PARAMETROS FIJOS')
print('lados: 2,4,6')
func_calPerTri(2,4,6)

print('---------------------------------------------')

print('LLAMADO A LA FUNCION CON PARAMETROS VARIABLES')
#captura de datos para el triangulo
lecLadUno=int(input('Digite el primer lado: ')) 
lecLadDos=int(input('Digite el segundo lado: '))
lecLadTres=int(input('Digite el tercer lado: '))

#llamado a la funcion
func_calPerTri(lecLadUno,lecLadDos,lecLadTres)
