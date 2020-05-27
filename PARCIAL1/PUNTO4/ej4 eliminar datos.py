
#============Definir las listas============
listAlum=[]   #lista de alumnos
listPes=[]   #lista de pesos
listAlt=[]   #lista de alturas
listGen=[]   #lista de generos
#==========Ingreso de valores=============
for x in range(3): #usamos el ciclo for para repertir las instrucciones siguientes 5 veces
    nom=input("Ingrese el nombre del alumno: ") #Ingresamos el nombre
    listAlum.append(nom) #añadimos el valor de la variable "nom" a la lista de nombres
    alt=float(input("Ingrese la altura de dicho alumno: ")) #ingresamos el valor de la altura
    listAlt.append(alt) #agregamos el valor de "alt" a la lista de alturas
    pes=int(input("ingrese el peso de dicho alumno: ")) #ingresamos el valor del peso
    listPes.append(pes)  #agregamos el valor de "pes" a la lista de pesos
    gen=input("Ingrese el genero del alumno: ") #Ingresamos el genero
    listGen.append(gen) #agregamos el valor de "gen" a la lista de generos
    
#===============INICIO DE ORDENAMIENTO DE DATOS=================================
for k in range(2): #usamos FOR para que repita lo siguiente se repita 4 veces
    for x in range(2-k): #usa FOR,haciendo que se repita 4 veces menos la posicion que tome k  
        if listAlt[x]<listAlt[x+1]: #colocamos un condicional,si el elemento de posicion x  de la lista de alutra es menor que el elemento siguiente(elemento x+1) en la misma lista de altura
            auxAlt=listAlt[x] #usamos "auxAlt" como una variable que acumula el elemento x de la lista de altura
            listAlt[x]=listAlt[x+1] #ahora la posicion del elemento cambia con la del elemento anterior
            listAlt[x+1]=auxAlt #se hace lo mismo para el resto de listas (nombres,peso, genero)    
            auxAlum=listAlum[x]
            listAlum[x]=listAlum[x+1]
            listAlum[x+1]=auxAlum
            auxPes=listPes[x]
            listPes[x]=listPes[x+1]
            listPes[x+1]=auxPes
            auxGen=listGen[x]
            listGen[x]=listGen[x+1]
            listGen[x+1]=auxGen
#Ordenamiento de las listas en formato de tabla
print("NOMBRE","ALTURA","PESO","SEX",sep="\t")
for i in range(len(listAlum)): #for que se repite tantas veces como elementos tenga la lista de nombres
    print(listAlum[i],listAlt[i],listPes[i],listGen[i],sep="\t")
    
nome="" #variable que almacena el nombre a eliminar
print("A quien desea eleminar?")
nome=input("Ingrese el nombre del alumno: ")
index=listAlum.index(nome) #variable que almacena la posicion en la lista del nombre que se va a eliminar
if listAlum[index]==nome:  #si el nombre almacenado en la lista es igual al nombre a eliminar, borrar todos los registro relacionados a dicho nombre
    listAlum.pop(index) #eliminar el nombre en la lista de alumnos en la posicion correspondiente
    listPes.pop(index) #eliminar el peso en la lista de peso en la posicion correspondiente 
    listAlt.pop(index) #eliminar la altura en la lista de altura en la posicion correspondiente 
    listGen.pop(index) #eliminar el genero en la lista de genero en la posicion correspondiente

#====================Ordenamiento de la lista sin el elemento eliminado =======================
for k in range(1):   #se realizan los mismos procedimientos del ordenamiento anterior
    for x in range(1-k):
        if listAlt[x]<listAlt[x+1]:
            auxAlt=listAlt[x]
            listAlt[x]=listAlt[x+1]
            listAlt[x+1]=auxAlt
            auxAlum=listAlum[x]
            listAlum[x]=listAlum[x+1]
            listAlum[x+1]=auxAlum
            auxPes=listPes[x]
            listPes[x]=listPes[x+1]
            listPes[x+1]=auxPes
            auxGen=listGen[x]
            listGen[x]=listGen[x+1]
            listGen[x+1]=auxGen
#Lista ordenada en formato de tablas sin el elemento eliminado
print("Lista de alumnos, sus alturas y sus pesos ordenados de mayor a menor")
print("NOMBRE","ALTURA","PESO","SEX",sep="\t")
for y in range(len(listAlum)):
    print(listAlum[y],listAlt[y],listPes[y],listGen[y],sep="\t")
