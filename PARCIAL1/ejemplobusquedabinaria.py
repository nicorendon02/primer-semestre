def busquedaBinaria(unaLista, item): #definimos la funcion de la busqueda binaria
    if len(unaLista) == 0: #si la cantidad de elementos de la lista es igual a cero
        return False #retorna "false"
    else:   #sino...
        punMed = len(unaLista)//2 #punto medio es igual a la cantidad de elementos de la lista dividida 2
        if unaLista[punMed]==item: #si el punto medio es igual al elemento que se esta buscando
          return True #retorna "true"
        else:
          if item<unaLista[punMed]: #si el elemento que se esta buscando es menor al punto medio 
            return busquedaBinaria(unaLista[:punMed],item) #se busca en los valores menores al punto medio hasta encontrar el elemento
          else: #si el elemento que se esta buscando es mayor al punto medio
            return busquedaBinaria(unaLista[punMed+1:],item) #se busca en los valores mayores al punto medio hasta encontrar el elemento

listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42] #lista que contiene los valores numericos
val=int(input('Ingrese el numero a buscar: ')) #se digita el valor que se quiere buscar
print(busquedaBinaria(listaPrueba, val)) # imprime "true" si el valor ingresado se encuentra en la lista o "false" si no está


