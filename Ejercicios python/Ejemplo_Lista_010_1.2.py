"""DECLARACION DE LISTAS"""
listNom=[]      #lista de nombres
listGen=[]      #lista de generos
listAlt=[]      #lista de alturas
listPes=[]      #lista de peso

"""DECLARACION DE CONTADORES"""
contador1=1     #contador del while
x=0             #contador de posicion de la lista
posList=0

"""DECLARACION DE VARIABLES"""
name=""         #nombre
alt=0.0         #altura
gen=""          #genero
pes=0           #peso

"""VARIABLES DE LOS HOMBRES"""
ttlHom=1      #total de hombres
ttlMuj=1
sumAltHom=0     #suma alturas hombres
promAltHom=0    #promedio altura hombres
sumPesHom=0     #suma peso hombres
promPesHom=0    #promedio pesos hombres
masAltoH=0
masAltoM=0
masBajoH=5
masBajoM=5
nombreMasAltoH=""
nombreMasALtoM=""
nombreMasBajoH=""
nombreMasBajoM=""
masPesoH=0
masPesoM=0
menPesoH=100
menPesoM=100
nombreMasPesoH=""
nombreMasPesoM=""
nombreMenPesoH=""
nombreMenPesoM=""

"""VARIABLES DE MUJERES"""
sumAltMuj=0     #suma alturas mujeres
promAltMuj=0    #promedio alturas mujeres
sumPesMuj=0     #suma pesos mujeres
promPesMuj=0    #promedio pesos mujeres

print('PARA TERMINAR ESCRIBA "FIN"')     #indica la forma de ingresar datos

name=input("Ingrese el nombre: ")        #se ingresa el nombre


"""INICIO DEL CICLO PARA DATOS DE LA LISTA"""

#=========INICIO DEL CICLO=============
while name.casefold()!="FIN".casefold():   #mientras el nombre sea diferente de "fin"...                   
    listNom.append(name)
    gen=input('Ingrese el genero, si es mujer(M) y si es hombre(H): ')
    listGen.append(gen)
    alt=float(input('Ingrese la altura: '))
    listAlt.append(alt)
    pes=int(input('Ingrese el peso: '))
    listPes.append(pes)
    name=input('Ingrese el nombre: ')

canEleList=len(listNom)
print('La cantidad de elementos de la lista es: ' + str (canEleList))

"""CICLO PARA LOS CALCULOS ACUMULADORES"""
posList=0
for posList in range (canEleList):
    print ('INGRESE AL FOR')
    if listGen[x].casefold()=='H'.casefold():
        print ('Es un hombre')
        ttlHom=ttlHom+1
        sumAltHom=sumAltHom+listAlt[posList]
        sumPesHom=sumPesHom+listPes[posList]
        print('Acumulador suma de altura hombres: ' + str(sumAltHom))
        print('la altura de esta posicion es: ' + str(listAlt[posList]))
        print('Acumulador suma de altura hombres: ' + str(sumAltHom))
    else:
        print(listGen[posList])
        ttlMuj=ttlMuj+1
        sumAltMuj=sumAltMuj+listAlt[posList]
        sumPesMuj=sumPesMuj+listPes[posList]
         

#========IMPRESION LISTA NOMBRES==========
posList=0
print('LISTA DE NOMBRES')
while posList < canEleList:
    print('posicion: ' + str (posList)+listNom[posList])
    ###33##3#
    posList=posList+1

#========IMPRESION LISTA GENEROS==========
posList=0
print('LISTA DE GENEROS')
while posList < canEleList:
    print('posicion: ' + str (posList) +  listGen[posList])
    posList=posList+1

#========IMPRESION LISTA ALTURAS==========
posList=0
print('LISTA DE ALTURAS')
while posList < canEleList:
    print('posicion: ' + str (posList) + str (listAlt[posList]))
    posList=posList+1

#========IMPRESION LISTA PESOS============
posList=0
print('LISTA DE PESO')
while posList < canEleList:
    print('posicion: ' + str (posList) + str (listPes[posList]))
    posList=posList+1

#======IMPRESION LISTAS PARALELAS========
while contador1 <= len (listNom):                   
    print(listNom[x] + '---' +str (listGen[x]) + '---' +str (listAlt[x]) + '---' +str (listPes[x]))
    x=x+1
    contador1=contador1+1

#==CALCULO DE PROMEDIOS POR SEPARADO=====

print('suma altura hombres'+str(sumAltHom))
print('suma altura mujeres'+str(sumAltMuj))
print('total hombres'+str(ttlHom))
print('total mujeres'+str(ttlMuj))


promAltHom=sumAltHom/ttlHom
promPesHom=sumPesHom/ttlHom
promAltMuj=sumAltMuj/ttlMuj
promPesMuj=sumPesMuj/ttlMuj
print('promedio peso hombres'+str(promPesHom))
print('promedio altura hombres'+str(promAltHom))
print('promedio altura mujeres'+str(promAltMuj))
print('promedio altura hombres'+str(promAltHom))

#========CALCULO DE PROMEDIOS GENERAL==========
sumAltTtl=sumAltHom+sumAltMuj
sumPesTtl=sumPesHom+sumPesMuj
promAltTtl=sumAltTtl/canEleList
promPesTtl=sumPesTtl/canEleList

if alt>masAltoH:
    masAltoH=alt
    nombreMasAltoH=name
if alt<masBajoH:
    masBajoH=alt
    nombreMasBajoH=name
if alt>masAltoM:
    masAltoM=alt
    nombreMasAltoM=name
if alt<masBajoM:
    masBajoM=alt
    nombreMasBajoM=name

if pes>masPesoM:
    masPesoM=pes
    nombreMasPesoM=name
if pes<masBajoH:
    masBajoH=pes
    nombreMenPesoH=name
if pes>menPesoM:
    menPesoM=pes
    nombreMenPesoM=name
if pes<menPesoH:
    MenPesoH=pes
    nombreMenPesoH=name
        

"""IMPRESION DE LISTAS POR SEPARADO"""
posList=0
print('LISTA DE NOMBRES')
while posList < canEleList:
    print('posicion: ' + 'a/tb' + str (posList) + 'a/tb' + str (listNom[posList]))
          
    posList=posList+1
          
while contador1 < len (listNom):                   
    print(listNom[x] + 'a/tb' +str (listGen[x]) + 'a/tb'  +str (listAlt[x]) + 'a/tb' +str (listPes[x]))
    x=x+1
    contador1=contador1+1

print('La cantidad de hombres es: '+str(ttlHom))                                #imprime la cantidad de hombres
print('El promedio de las alturas de los hombres es: ' + str (promAltHom))      #imprime el promedio altura hombres
print('El promedio del peso de los hombres es: ' + str (promPesHom))            #imprime el promedio peso hombres
print('La cantidad de mujeres es: '+str(ttlMuj))                                #imprime cantidad de mujeres
print('El promedio de las alturas de las mujeres es: ' + str (promAltMuj))      #imprime promedio altura mujeres
print('El promedio del peso de las mujeres es: ' + str (promPesMuj))            #imprime el promedio peso mujeres
print (nombreMasAltoH)
print(nombreMenPesoM)
print(nombreMasPesoH)
#========FIN DE LA IMPRESION==========
#end
