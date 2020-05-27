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