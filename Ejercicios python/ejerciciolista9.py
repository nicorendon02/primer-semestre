lista=[]
valor=int(input("Ingresar valor (0 para finalizar):"))
while valor!=0:  # !# significa "diferente de"
    lista.append(valor)  # .append almacena el valor ingresado a la ultima posicion de la lista
    valor=int(input("Ingresar valor (0 para finalizar):"))

print("Tamano de la lista:")
print(len(lista))
