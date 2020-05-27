"""CALCULOS CON LISTAS"""
lisNom=[]      #lista para nombres
lisGen=[]      #lista para generos
lisAlt=[]      #lista para alturas
lisPes=[]      #lista para pesos
#=======CONTADORES============
conCic=1       #contador del ciclo
x=0             #contador de posicion en lista
#DECLARACION DE VARIABLES=====
nom=""         #nombra
alt=0.0         #altura
gen=""          #genero
pes=0           #peso
#====VARIABLES HOMBRES========
totHom=0        #total hombres
sumAltHom=0     #suma alturas hombres
promAltHom=0    #promedio altura hombres
sumPesHom=0     #suma peso hombres
promPesHom=0    #promedio peso hombres
#====VARIABLES MUJERES========
totMuj=0        #total mujeres
sumAltMuj=0     #suma alturas mujeres
promAltMuj=0    #promedio altura mujeres
sumPesMuj=0     #suma pesos mujeres
promPesMuj=0    #promedio peso mujeres
#=============================
print('PARA TERMINAR ESCRIBA "FIN"')     #instruccion para el ingreso de datos
nom=input("Ingrese el nombre: ")        #ingreso del nombre
#====INICIO DEL CICLO=========
while nom.casefold()!="FIN".casefold():     #mientras el nombre no sea "fin"... 
    lisNom.append(nom)
    gen=input('Ingrese el genero, si es mujer(M) y si es hombre(H): ')
    lisGen.append(gen)
    alt=float(input('Ingrese la altura: '))
    lisAlt.append(alt)
    pes=int(input('Ingrese el peso: '))
    lisPes.append(pes)
    nom=input('Ingrese el nombre: ')

    if gen.casefold()=='H'.casefold():         #si el genero es masculino...
        totHom=totHom+1
        sumAltHom=sumAltHom+alt
        promAltHom=sumAltHom/totHom
        sumPesHom=sumPesHom+pes
        promPesHom=sumPesHom/totHom
    else:                               #si el genero es femenino...
         totMuj=totMuj+1
         sumAltMuj=sumAltMuj+alt
         promAltMuj=sumAltMuj/totMuj
         sumPesMuj=sumPesMuj+pes
         promPesMuj=sumPesMuj/totMuj
#====FIN DEL CICLO===========
"""ZONA DE IMPRESIONES"""
print('NOMBRE --- GENERO --- ALTURA --- PESO')      #imprime los titulos de la lista en paralelo

while conCic <= len (lisNom):                   #ciclo para imprimir en orden los datos de la lista paralela
    print(lisNom[x] + '---' +str (lisGen[x]) + '---' +str (lisAlt[x]) + '---' +str (lisPes[x]))
    x=x+1
    conCic=conCic+1

print('La cantidad de hombres es: '+str(totHom))                                #imprime la cantidad de hombres 
print('El promedio de las alturas de los hombres es: ' + str (promAltHom))      #imprime el promedio de altura hombres
print('El promedio del peso de los hombres es: ' + str (promPesHom))            #imprime el promedio de peso hombres
print('La cantidad de mujeres es: '+str(totMuj))                                #imprime la cantidad de mujeres
print('El promedio de las alturas de las mujeres es: ' + str (promAltMuj))      #imprime el promedio de altura mujeres
print('El promedio del peso de las mujeres es: ' + str (promPesMuj))            #imprime el promedio peso mujeres
#end
