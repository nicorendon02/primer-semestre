lisFib=[]
def fib_i(n):   #define la función para fib
    a, b = 0, 1   # variables a y b toman valores de 0 y 1
    while n > 0:   #mientras n sea mayor a 0...
        a, b = b, a + b   #opera con sumas la sucesion en a y b
        n -= 1   # n va disminuyendo
    return a   #devuelve a

def func_LlamadaFib():
    num=int(input(" Ingrese el numero final de la sucesion: "))   #pide el límite de la sucesion
    for i in range(num):   # para i en el rango del número digitado...
        lisFib.append(fib_i(i))   #lo guarda en la lista de resultados...
    return lisFib   #retorna la lista
print(func_LlamadaFib())   #llamado a la función
