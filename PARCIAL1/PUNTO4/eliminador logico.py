#==========================Definir las listas===================================
listAlum=[]   #lista de alumnos
listPes=[]   #lista de pesos
listAlt=[]   #lista de alturas
listGen=[]   #lista de generos
listEstado=[]   #lista de estados
#===========================Ingreso de valores==================================
for x in range(3): #usamos el ciclo for para repertir las instrucciones siguientes 5 veces
    nom=input("Ingrese el nombre del alumno: ") #Ingresamos el nombre
    listAlum.append(nom) #añadimos el valor de la variable "nom" a la lista de nombres
    alt=float(input("Ingrese la altura de dicho alumno: ")) #ingresamos el valor de la altura
    listAlt.append(alt) #agregamos el valor de "alt" a la lista de alturas
    pes=int(input("ingrese el peso de dicho alumno: ")) #ingresamos el valor del peso
    listPes.append(pes)  #agregamos el valor de "pes" a la lista de pesos
    gen=input("Ingrese el genero del alumno: ") #Ingresamos el genero
    listGen.append(gen) #agregamos el valor de "gen" a la lista de generos
    listEstado.append("true")   #recibe 'true' en la lista de estados
    
#===============INICIO DE ORDENAMIENTO DE DATOS=================================
for k in range(2): #usamos FOR para que repita lo siguiente se repita 4 veces
    for x in range(2-k): #usa FOR,haciendo que se repita 4 veces menos la posicion que tome k  
        if listAlt[x]<listAlt[x+1]: #colocamos un condicional,si el elemento de posicion x  de la lista de alutra es menor que el elemento siguiente(elemento x+1) en la misma lista de altura
            auxAlt=listAlt[x] #usamos "aux1" como una variable que acumula el elemento x de la lista de altura
            listAlt[x]=listAlt[x+1] #ahora la posicion del elemento cambia con la del elemento anterior
            listAlt[x+1]=auxAlt   #la posicion de la altura siguiente va para el auxiliar
            #se hace lo mismo para el resto de listas (nombres,peso, genero)    
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
    print(listAlum[i],listAlt[i],listPes[i],listGen[i],sep="\t") #listas tabuladas
    
nome="" #variable que almacena el nombre a eliminar
print("A quien desea eleminar?")   #pregunta a quien desea eliminar
nome=input("Ingrese el nombre del alumno: ") #nombre de la persona a eliminar
index=listAlum.index(nome) #index retorna la posicion en la que se encuentre la variable "nome" en la lista de alumnos
listEstado[index]="false" #cambia el estado en la lista de estados en la posicion que se encuentre "nome"
#se imprime la tabla con eliminado lógico
print("ELIMINADO LÓGICO")   #imprime el titulo de la lista
print("NOMBRE","ALTURA","PESO","SEX",sep="\t")   #imprime los titulos de las listas paralelas
for y in range(len(listAlum)):   #para una variable y en el rango de la cantidad de elementos de la lista de alumnos...
    if listEstado[y]=="true": #si el estado es "true" imprime las listas activas
        print(listAlum[y],listAlt[y],listPes[y],listGen[y],"Activo  ",listEstado[y],sep="\t")   #impresion de listas activas
    else: #si no, es decir, si es "false" imprimir las listas "borradas"
        print(listAlum[y],listAlt[y],listPes[y],listGen[y],"Borrado ",listEstado[y],sep="\t")   #impresion de listas 'borradas'
        
indexElim=listEstado.index("false") #busca en la lista de estado "false" y retorna la posicion
listAlum.pop(indexElim) #en la lista de alumnos borra en la posicion que tenga "indexElim" el nombre 
listPes.pop(indexElim)  #en la lista de peso borra en la posicion que tenga "indexElim" el peso
listAlt.pop(indexElim)  #en la lista de altura borra en la posicion que tenga "indexElim" la altura
listGen.pop(indexElim) #en la lista de genero borra en la posicion que tenga "indexElim" el genero
listEstado.pop(indexElim) #en la lista de estado borra en la posicion que tenga "indexElim" el estado
#se imprime la tabla con eliminado físico
print("")   #se imprime un separador de las dos tablas
print("ELIMINADO FÍSICO")   #se imprime el titulo de la tabla
print("NOMBRE","ALTURA","PESO","SEX",sep="\t")     #se imprimen los titulos de las listas paralelas   
for f in range(len(listAlum)):   #mientras se cumpla el rango de la cantidad de elementos de la lista alumnos...
    if listEstado[f]=="true":   #si la lista de estado es 'true'...
        print(listAlum[f],listAlt[f],listPes[f],listGen[f],"Activo  ",listEstado[f],sep="\t") #Tablas tabuladas sin el elemento eliminado
