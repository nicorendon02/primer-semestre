#============Definir las listas=================================================
listAlum=[]   #lista de alumnos
listPes=[]   #lista de pesos
listAlt=[]   #lista de alturas
listGen=[]   #lista de generos
#==========Ingreso de valores===================================================
for x in range(3): #usamos el ciclo for para repertir las instrucciones siguientes 5 veces
    nom=input("Ingrese el nombre del alumno: ") #Ingresamos el nombre
    listAlum.append(nom) #añadimos el valor de la variable "nom" a la lista de nombres
    alt=float(input("Ingrese la altura de dicho alumno: ")) #ingresamos el valor de la altura
    listAlt.append(alt) #agregamos el valor de "alt" a la lista de alturas
    pes=int(input("ingrese el peso de dicho alumno: "))#ingresamos el valor del peso
    listPes.append(pes)#agregamos el valor de "pes" a la lista de pesos
    gen=input("Ingrese el genero del alumno: ")#Ingresamos el genero
    listGen.append(gen)#agregamos el valor de "gen" a la lista de generos
#===============INICIO DE ORDENAMIENTO DE DATOS=================================
for k in range(2): #usamos FOR para que repita lo siguiente se repita 4 veces
    for x in range(2-k): #usa FOR,haciendo que se repita 4 veces menos la posicion que tome k  
        if listAlt[x]<listAlt[x+1]: #colocamos un condicional,si el elemento de posicion x  de la lista de alutra es menor que el elemento siguiente(elemento x+1) en la misma lista de altura
            auxAlt=listAlt[x] #usamos "auxAlt" como una variable que acumula el elemento x de la lista de altura
            listAlt[x]=listAlt[x+1] #ahora la posicion del elemento cambia con la del elemento siguiente
            listAlt[x+1]=auxAlt    #el auxiliar toma el valor del elemento siguiente
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
print('Vista previa de la tabla')   #imprime un aviso
print('NOM --- ALT --- PES --- GEN')  #imprime los titulos de la tabla
for x in range(len(listAlum)):  #for que se repite tantas veces como elementos tenga la lista de nombres
    print(listAlum[x],listAlt[x],listPes[x],listGen[x],sep="\t")   #imprime las listas paralelas y tabula

print('¿Desea modificar algún dato?')  #imprime un aviso
mod=input('Diga SI o NO: ')         #el usuario ingresa una respuesta

if mod.casefold()=='SI'.casefold():   #si el usuario desea modificar datos...
    cambio=""   #se declara una variable
    while cambio.casefold()!="fin".casefold():   #mientras cambio sea diferente de fin...
        cambio=input("¿Que desea modificar? (nombre, altura, peso, genero) ingrese (fin) para dejar de modificar: ")  #imprime un aviso
        if cambio.casefold()=="nombre".casefold():   #si el usuario desea cambiar un nombre...
            nomNom=input("Ingrese la persona para cambiar el nombre: ")   #pregunta por la persona a la que se le va a cambiar el nombre
            indexNom=listAlum.index(nomNom)   #pide la posicion del nombre en la lista
            nomMod=input("Ingrese el nuevo nombre: ")  #se ingresa el nuevo nombre
            listAlum[indexNom]=nomMod   #pone el nuevo nombre en la posicion del nombre antiguo
        elif cambio.casefold()=="altura".casefold():   #si el usuario quiere cambiar la altura...
            altNom=input("Ingrese la persona para cambiar la altura: ")   #pregunta por la persona a la que le va a cambiar la altura
            indexAlt=listAlum.index(altNom)   #llama a la posicion de ese nombre en la lista
            altMod=float(input("Ingrese el nuevo valor de la altura: "))  #se ingresa la nueva altura
            listAlt[indexAlt]=altMod   #guarda la nueva altura en la posicion de la altura antigua
        elif cambio.casefold()=="peso".casefold():   #si el usuario quiere cambiar el peso...
            genNom=input("Ingrese la persona para cambiar el peso: ")   #pregunta por la persona a la que se le va a cambiar el peso
            indexPes=listAlum.index(genNom)   #llama la posicion del peso solicitado dentro de la lista
            pesMod=int(input("Ingrese el nuevo valor del peso: "))   #se ingresa el nuevo peso
            listPes[indexPes]=pesMod   #pone el nuevo peso en la posicion del peso antiguo
        else:
            if cambio.casefold()=="genero".casefold():   #si la persona quiere cambiar el genero...
                genNom=input("Ingrese la persona para cambiar el genero: ")   #se pregunta por la persona a la que se le quiere cambiar el genero
                indexGen=listAlum.index(genNom)   #pide la posicion del genero solicitado
                genMod=input("Ingrese el nuevo valor del genero: ")   #se ingresa el nuevo genero
                listGen[indexGen]=genMod   #el nuevo genero ocupa la posicion del antiguo en la lista
            

 #======= Ordenamiento de los valores incluyendo los nuevos datos agregados=======
for k in range(2):    #Se realizan los mismos procesos de ordenamiento anteriores
    for x in range(2-k):   #usa FOR,haciendo que se repita 4 veces menos la posicion que tome k
        if listAlt[x]<listAlt[x+1]:   #si la altura en la posicion actual es mayor al dato siguiente...
            auxAlt=listAlt[x]   #usamos "auxAlt" como una variable que acumula el elemento x de la lista de altura
            listAlt[x]=listAlt[x+1]   #ahora la posicion del elemento canbia con la del elemento siguiente
            listAlt[x+1]=auxAlt     #el auxiliar toma el valor del elemento siguiente
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
#====== Ordenamiento de los datos en formato de tablas ===========================         
print("Lista de alumnos, sus alturas y sus pesos ordenados de mayor a menor") #se imprime una lista
print('NOM --- ALT --- PES --- GEN')   #se imprimen los titulos de la lista
for x in range(len(listAlum)):  #se inicia un ciclo tomando como base la cantidad de elementos en la lista de alumnos
    print(listAlum[x],listAlt[x],listPes[x],listGen[x],sep="\t")  #imprime las listas paralelas y tabula
