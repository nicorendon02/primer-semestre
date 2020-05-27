lista=[1000, 6000, 400, 23, 130, 400, 60, 2000]
canMayCien=0
canMenCien=0
numMayCien=0
numMenCien=0
x=0
while x<len(lista):
    if lista[x]>100:
        canMayCien=canMayCien+lista[x]
        numMayCien=numMayCien+1
    else:
        canMenCien=canMenCien+lista[x]
        numMenCien=numMenCien+1
    x=x+1
    
print("La lista esta constituida por los elementos:")
print(lista)
print("La cantidad de valores mayores a 100 en la lista son:")
print(canMayCien)
print('y son: '+str(numMayCien))
print("La cantidad de valores menores a 100 en la lista son:")
print(canMenCien)
print('y son: '+str(numMenCien))

