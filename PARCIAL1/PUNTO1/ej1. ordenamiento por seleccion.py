import random    #importa datos aleatorios para la lista
#=======LISTA1=============================================================
lisX=[]                  #definimos la lista
#=========INGRESO DE VALORES===============================================
for x in range(10):       #usamos el FOR para repetir 10 veces(10 valores)
    valor=random.randrange(100)    #ingresamos un valor
    lisX.append(valor)   #añadimos el valor a la lista respectiva
#=============PROCESO DE ORDENAMIENTO======================================
def ordenamientoPorSeleccion(lisX):        #definimos el tipo de ordenamiento
   for llenarRanura in range(len(lisX)-1,0,-1):   #usamos FOR para repetir lo siguiente dependiendo del numero de elementos de la lista(en este caso 10)
       posicionDelMayor=0             #definimos un acumulador igualado a 0
       for ubicacion in range(1,llenarRanura+1):     #usa FOR para que "ubicacion" se repita, desde 1 hasta la misma cantidad de veces que se repite "rellenar ranura" y le sumamos 1
           if lisX[ubicacion]>lisX[posicionDelMayor]: #colocamos un condicional, si un elemento x es mayor que el elemto mayor(en este caso empieza siendo 0)
               posicionDelMayor = ubicacion    #el condicional anterior hace que la posicion del elemento(en este  caso x) queda siendo la posicion del elemento mas grande de la lista
#EN POCAS PALABRAS, EL PROGRAMA BUSCA EL ELEMENTO MAYOR DE LA LISTA Y EL ULTIMO
       temp = lisX[llenarRanura]    #usamos un acumulador "temp" para acumular el ultimo elemento de la lista, el cual deja su posicion libre
       lisX[llenarRanura] = lisX[posicionDelMayor]   #hacemos un intercambio donde la posicion del ultimo elemento la ocupa el elemento mayor
       lisX[posicionDelMayor] = temp   #otro intercambio donde el elemento acumulado en temp(el ultimo elemento) toma el lugar que ocupaba el elemento mayor de la lista
#=======TODO ESTE PROCESO SE REPITE HASTA QUE LA LISTA QUEDE EN ORDEN(MENOR A MAYOR)============
ordenamientoPorSeleccion(lisX)   
#=============FIN ORDENAMIENTO, AHORA LA IMPRESION DE LA LISTA(SALIDA)=====
print(lisX)   #imprime la lista

