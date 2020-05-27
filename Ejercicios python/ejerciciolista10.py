"""LISTA DE ENTEROS"""
lisEnt=[]
suma=0
for x in range(2,2002,2):
    lisEnt.append(x)
    suma=suma+x
prom=suma/1000
print(lisEnt)
print('la suma de los valores es: '+str(suma))
print('el promedio es: '+str(prom))
