def busquedaSecuencial(lisVal,val): #función de busquedalineal, recibe la lista y el elemento que estamos buscando
    i=0  #variable que almacenará la pos del elemento
    for x in lisVal:   #ciclo para la búsqueda
        if (x == val): #si 'x' es igual al elemento que estamos buscando...
            return i  #se retorna la posicion de ese elemento
        i=i+1  #contador de vueltas
    return -1  #retorna '-1' si no encuentra el elemento

def main():  #definir función principal "main"
    lisVal=[11,22,33,44,55,66,77,88,99]  #se define la lista
    val=int(input('Ingrese el valor que quiere buscar: ')) #se digita el valor que se quiere buscar
    pos=busquedaSecuencial(lisVal,val) #metodo de busqueda lineal al que se le pasa la lista y el elemento que estamos buscando, y retorna la posición
    if (pos>-1): #si posición es mayor que -1...
        print('La posición es: ',pos,'(True)') #imprime la posición del elemento encontrado
    else:   #sino...
        print('El elemento no se encuentra en la lista','(False)') #aviso que indica que no se encontró el elemento

main()  #se llama a la función principal
