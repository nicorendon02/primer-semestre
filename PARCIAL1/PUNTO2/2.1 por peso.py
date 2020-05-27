#======DEFINIMOS LAS LISTAS=====================================================
listAlum=[]  #lista de alumnos
listPes=[]   #lista de pesos
listAlt=[]   #lista de alturas
listGen=[]   #lista de generos
#===============NGRESO DE DATOS=================================================
for x in range(5):
    nom=input("Ingrese el nombre del alumno: ")#ingresamos nombre(variable)
    listAlum.append(nom)#añadimos el nombre a la lista de nombres
    alt=float(input("Ingrese la altura de dicho alumno: "))#ingresamos  altura(variable)
    listAlt.append(alt)#añadimos la altura a la lista de alturas
    pes=int(input("ingrese el peso de dicho alumno: "))#ingresamos peso(variable)
    listPes.append(pes)#añadimos el peso en la lista de pesos
    gen=input("Ingrese el genero del alumno: ")#ingrese el genero(variable)
    listGen.append(gen)#añadimos el genero a la lista de generos


#impresion de la lista sin ordenar por peso
print('VISTA PREVIA SIN ORDENAR')
print("NOMBRE","ALTURA","PESO","SEX",sep="\t")
for x in range(len(listAlum)): #usa el FOR para que la siguiente impresion se repita la cantidad de nombres que hay en la lista nombres
               print(listAlum[x],listAlt[x],listPes[x],listGen[x],sep="\t") #imprime el elemto x de: lista nombres,alturas,pesos y generos. y tabula la informacion.


#===============INICIO DE ORDENAMIENTO DE DATOS=================================
for k in range(4): #usamos FOR para que repita lo siguiente se repita 4 veces
    for x in range(4-k): #usa FOR,haciendo que se repita 4 veces menos la posicion que tome k        
        if listPes[x]<listPes[x+1]: #colocamos un condicional,si el elemento de posicion x  de la lista de peso es menor que el elemento siguiente(elemento x+1) en la misma lista de peso
            auxPes=listPes[x]  #usamos "auxPes" como una variable que acumula el elemento x de la lista de peso
            listPes[x]=listPes[x+1] #ahora la posicion del elemento x de la lista de pesos la ocupa el elemento siguiente(x+1)de la lista de peso
            listPes[x+1]=auxPes #auxPes(elemento x de la lista peso) toma el lugar que antes ocupaba el elemento siguiente(x+1) de la lista peso
            auxAlum=listAlum[x]  #usamos auxAlum como acumulador del elemento x de la lista de nombres
            listAlum[x]=listAlum[x+1] #ahora la posicion del elemento x de la lista de nombres la ocupa el elemento siguiente(x+1)de la lista de nombres
            listAlum[x+1]=auxAlum #auxAlum(elemento x de la lista nombres) toma el lugar que antes ocupaba el elemento siguiente(x+1) de la lista nombres
            auxAlt=listAlt[x] #usamos auxAlt como acumulador del elemento x de la lista de alturas
            listAlt[x]=listAlt[x+1] #ahora la posicion del elemento x de la lista de alturas la ocupa el elemento siguiente(x+1)de la lista de alturas
            listAlt[x+1]=auxAlt #auxAlt(elemento x de la lista alturas) toma el lugar que antes ocupaba el elemento siguiente(x+1) de la lista alturas
            auxGen=listGen[x] #usamos auxGen como acumulador del elemento x de la lista de generos
            listGen[x]=listGen[x+1]#ahora la posicion del elemento x de la lista de generos la ocupa el elemento siguiente(x+1)de la lista de generos
            listGen[x+1]=auxGen #auxGen(elemento x de la lista generos) toma el lugar que antes ocupaba el elemento siguiente(x+1) de la lista generos
#==============FIN ORDENAMIENTO, SIGUE LA IMPRESION DE DATOS(SALIDA)=============================
print("Lista de alumnos, sus alturas y sus pesos ordenados de mayor a menor")
print("NOMBRE","ALTURA","PESO","SEX",sep="\t")
for x in range(len(listAlum)): #usa el FOR para que la siguiente impresion se repita la cantidad de nombres que hay en la lista nombres
               print(listAlum[x],listAlt[x],listPes[x],listGen[x],sep="\t") #imprime el elemto x de: lista nombres,alturas,pesos y generos. y tabula la informacion.
