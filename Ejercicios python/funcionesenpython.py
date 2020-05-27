#1.0 funciones matematicas
print('1. FUNCIONES MATEMATICAS')
# 1.1 floor()
print('FUNCION FLOOR()')
import math #Este módulo proporciona acceso a las funciones matemáticas definidas por el estándar
print ("math.floor(-23.11) : ", math.floor(-23.11))
print ("math.floor(300.16) : ", math.floor(300.16))
print ("math.floor(300.72) : ", math.floor(300.72)) 
#El método floor () en Python devuelve el entero más grande no mayor que x.

print('-------------------------------------------------------------------')
# 1.2 ceil()
print('FUNCION CEIL()')
import math #Este módulo proporciona acceso a las funciones matemáticas definidas por el estándar
print ("math.ceil(-23.11) : ", math.ceil(-23.11))
print ("math.ceil(300.16) : ", math.ceil(300.16))
print ("math.ceil(300.72) : ", math.ceil(300.72))
#El método ceil () en Python devuelve el entero más pequeño, no menor que x.

print('-------------------------------------------------------------------')
# 1.3 fabs()
print('FUNCION FABS()')
import math #Este módulo proporciona acceso a las funciones matemáticas definidas por el estándar
print ("math.fabs(-11) : ", math.fabs(-11))
print ("math.fabs(22) : ", math.fabs(22))
print ("math.fabs(-52) : ", math.fabs(-52))
#El metodo fabs() devuelve el valor absoluto del numero en cuestión.

print('-------------------------------------------------------------------')
# 1.4 pow()
print('FUNCION POW()')
import math #Este módulo proporciona acceso a las funciones matemáticas definidas por el estándar
print ("math.pow(2^2) : ", math.pow(2,2)) #se usa (numero,potencia)
print ("math.pow(3^2) : ", math.pow(3,2))
print ("math.pow(5^2) : ", math.pow(5,2))
#El metodo pow() devuelve la potencia asignada del numero en cuestión.

print('-------------------------------------------------------------------')
# 1.5 factorial()
print('FUNCION FACTORIAL()')
import math #Este módulo proporciona acceso a las funciones matemáticas definidas por el estándar
print ("math.factorial(2) : ", math.factorial(2))
print ("math.factorial(4) : ", math.factorial(4))
print ("math.factorial(6) : ", math.factorial(6))
#El metodo factorial() devuelve el factorial del numero en cuestión.

print('-------------------------------------------------------------------')
#2.0 funciones de texto
print('2. FUNCIONES TEXTO')

# 2.1 lower()
print('FUNCION LOWER()')
var1 = "ESTOY EN LA U!"  #declara variable
print(var1.lower())
#El lower convierte todo el texto comparado a minusculas para evitar errores.

print('-------------------------------------------------------------------')

# 2.2 upper()
print('FUNCION UPPER()')
var1 = "estoy en la u!"  #declara variable
print(var1.upper())
#El upper convierte todo el texto comparado a mayusculas para evitar errores.

print('-------------------------------------------------------------------')

# 2.3 casefold()
print('FUNCION CASEFOLD()')
var1 = "estoy en la u!"  #declara variable
var2 = "ESTOY EN LA U!"  #declara variable
if var1.casefold()==var2.casefold():
    print('Son iguales')
else:
    print('No son iguales')
#El casefold() no discrimina entre mayusculas y minusculas las variables comparadas.

print('-------------------------------------------------------------------')

# 2.4 capitalize()
print('FUNCION CAPITALIZE()')
var1 = "estoy en la u!"  #declara variable
print(var1.capitalize())
#El capitalize() solo pone en mayuscula la primera letra.

print('-------------------------------------------------------------------')

# 2.5 swapcase()
print('FUNCION SWAPCASE()')
var1 = "estoy en la u!"  #declara variable
var2 = "ESTOY EN LA U!"  #declara variable
print(var1.swapcase())
print(var2.swapcase())
#El swapcase() cambia lo que esta en mayuscula a minuscula y viceversa.

print('-------------------------------------------------------------------')

# 2.6 title()
print('FUNCION TITLE()')
var1 = "estoy en la universidad"  #declara variable
print(var1.title())
#El title() escribe en mayúsculas solo la primera letra de cada palabra.

print('-------------------------------------------------------------------')

# 3.0 funciones fecha/hora
print("3. FUNCIONES DE TIEMPO")
# 3.1 funcion .altzone
#===================FUNCION .ALTZONE=================
import time #importa el tiempo
print("FUNCION .ALTZONE")
print ("time.altzone:  "  +str(time.altzone)) #devuelve el número de segundos  del desplazamiento  tiempo en la zona de West Greenwich luz del día.
#====================FIN .ALTZONE====================
print('-------------------------------------------------------------------')
# 3.2 funcion asctime()
#===================FUNCION ASCTIME()================
print("FUNCION .ASCTIME")
t = time.localtime() # Establecemos nuestra tupla, la cual será obtenida por localtime.

print ("time.asctime(t): %s " % time.asctime(t)) #lo convierte en una cadena de caracteres  de tipo “Mon Jul 30 15:16:04 1997”.
#==================FIN FUNCION ASCTIME()=============
print('-------------------------------------------------------------------')
# 3.3 funcion time.time()
#==================FUNCION TIME.TIME()================
print("FUNCION TIME.TIME")
t0 = time.time()

print (time.time() - t0, "seconds wall time")
#Este método nos devuelve el tiempo como un número tipo float expresado en segundos desde la época en UTC.
#=================FIN FUNCION TIME.TIME()=============
print('-------------------------------------------------------------------')
# 3.4 funcion time.gmtime()
#==============FUNCION TIME.GMTIME====================
print("FUNCION .GTIME")
print ("time.gmtime() :"+str( time.gmtime()))
#El método gmtime() nos convierte el tiempo expresado en segundos de una época a una struct_time en UTC(tiempo coordenaod universal)
#=============FIN FUNCION  TIME.GMTIME===============
print('-------------------------------------------------------------------')
# 3.5 funcion time.localtime()
#============FUNCION TIME.LOCALTIME===================
print("FUNCION .LOCALTIME")
print ("time.localtime() :"+ str( time.localtime()))
#El método localtime() es muy parecido a gmtime(), pero en este no obtenemos los segundos de la hora local.
print('-------------------------------------------------------------------')

# 4.0 funciones estadistica
print('4. FUNCIONES ESTADISTICA')

# 4.1 funcion .mean
print("FUNCION .MEAN")
import statistics as stats
edades = [22, 23, 26, 26, 26, 34, 34, 38, 40, 41]
print(stats.mean(edades))  # suma los elementos de la lista y los divide entre la cantidad de elementos(media aritmetica)
print('-------------------------------------------------------------------')
# 4.2 funcion .median
print("FUNCION .MEDIAN")
edades = [22, 23, 26, 26, 26, 34, 34, 38, 40, 41]
print(stats.median(edades))  # imprime el valor de la mitad, si es par saca el promedio de los dos numeros centrales y esa es la media
print('-------------------------------------------------------------------')
# 4.3 funcion .mode
print("FUNCION .MODE")
edades = [22, 23, 26, 26, 26, 34, 34, 38, 40, 41]
print(stats.mode(edades))  # saca el valor mas repetido de la lista (moda)
print('-------------------------------------------------------------------')
# 4.4 funcion .median_grouped
print("FUNCION .MEDIAN_GROUPED")
datos=[1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6]
print(stats.median_grouped(datos))
#devuelve el valor de la mitad, en datos agrupados(Posición_de_mediana = (número_de_datos + 1) / 2) y luego se suman los dos numeros
print('-------------------------------------------------------------------')
# 4.5 funcion .pvariance
print("FUNCION .PVARIANCE")
edades = [22, 23, 26, 26, 26, 34, 34, 38, 40, 41]
print(stats.pvariance(edades))  # representa la variabilidad de los datos respecto a la media
