import random    #importa valores aleatorios para la lista
#========================================DEFINIR LISTA==========================================
lisX=[]   #se define la lista
#=====================================INGRESO DE VALORES========================================
for x in range(10):           #usamos el FOR  para repetir 10 veces(10 valores)
    valor=random.randrange(100)   #ingresamos un valor
    lisX.append(valor)   #añadimos el valor a la lista respectiva
#=====================================PROCESO DE ORDENAMIENTO===================================
def ordenamientoDeShell(lisX):   #definimos el tipo de ordenamiento
    contadorSublistas = len(lisX)//2  #abrimos un  contador de sublistas dividiendo la cantidad de elementos de las listas entre 2
    while contadorSublistas > 0:    #mientras el contador de sublistas sea mayor a 0  

      for posicionInicio in range(contadorSublistas):    #usamos FOR para que se repita tantas veces como sublistas
        brechaOrdenamientoPorInsercion(lisX,posicionInicio,contadorSublistas) #comienza el ordenamiento por insercion


      contadorSublistas = contadorSublistas // 2   #abrimos otro contador de sublistas dividiendo la cantidad de sublistas entre 2

def brechaOrdenamientoPorInsercion(lisX,inicio,brecha):   #definimos la brecha
    for i in range(inicio+brecha,len(lisX),brecha):    #inicio del ciclo

        valorActual = lisX[i]   #el valor actual toma la posicion i de la lista
        posicion = i     #la posicion sera igual al valor actual de i

        while posicion>=brecha and lisX[posicion-brecha]>valorActual:   #mientras la posicon sea mayor o igual que la brecha y el elemento(posicion-brecha) sea mayor al valor actual...
            lisX[posicion]=lisX[posicion-brecha]    #la posicion actual de la lista tomara el valor de (posicion-brecha)
            posicion = posicion-brecha    #posicion es igual a (posicion-brecha)
#=======TODO ESTE PROCESO SE REPITE HASTA QUE LA LISTA QUEDE EN ORDEN(MENOR A MAYOR)===========
        lisX[posicion]=valorActual     #la posicion actual de la lista es igual al valorActual
ordenamientoDeShell(lisX)
#=============FIN ORDENAMIENTO, AHORA LA IMPRESION DE LA LISTA(SALIDA)=========================
print(lisX)   #imprime la lista
