#DECALARA LISTA
listNom=[]      #LISTA DE NOMBRES
listGen=[]      #LISTA DE GENEROS
listAlt=[]      #LISTA DE ALTURAS
listPes=[]      #LISTA DE PESO

#CONTADORES
contador1=1     #CONTADOR DEL WHILE
x=0             #CONTADOR DE LA POSICIÓN EN LA QUE SE ENCUENTRA LA LISTA

#DECLARA LAS VARIABLES GENERAL
name=""         #NOMBRE
alt=0.0         #ALTURA
gen=""          #GENERO
pes=0           #PESO

#VARIABLES DE LOS HOMBRES
ttlHom=0        #TOTAL DE HOMBRES
sumAltHom=0     #SUMA DE DE LAS ALTURAS DE LOS HOMBRES
promAltHom=0    #PROMEDIO DE LA ALTURA DE LOS HOMBRES
sumPesHom=0     #SUMA DEL PESO DE LOS HOMBRES
promPesHom=0    #PROMEDIO DEL PESO DE LOS HOMBRES

#VARIABLES DE LAS MUJERES
ttlMuj=0        #TOTAL DE HOMBRES
sumAltMuj=0     #SUMA DE LAS ALTURAS DE LAS MUJERES
promAltMuj=0    #PROMEDO DE LAS ALTURAS DE LAS MUJERES
sumPesMuj=0     #SUMA DE LOS PESOS DE LAS MUJERES
promPesMuj=0    #PROMEDIO DE LOS PESOS DE LAS MUJERES

print('PARA TERMINAR UTILICE "FIN"')     #IMPRIME LA FORMA DE COMO TERNIMAR DE INGRESAR DATOS

name=input("Ingrese el nombre: ")        #PIDE QUE INGRESE EL NOMBRE DE LA PERSONA PARA PODER INICIAR EL PRIMER CICLO WHILE

while name != "FIN":                     #ESTE CICLO SE ENCARGA DE PEDIR LA INFORMACIÓN DE TODAS LAS PERSONAS CON LAS QUE SE DESEA TRABAJAR 
    listNom.append(name)
    gen=input('Ingrese el genero, si es mujer(M) y si es hombre(H): ')
    listGen.append(gen)
    alt=float(input('Ingrese la altura: '))
    listAlt.append(alt)
    pes=int(input('Ingrese el peso: '))
    listPes.append(pes)
    name=input('Ingrese el nombre: ')

    if gen == 'H':                      #ESTE CODICIONAL SELECCIONA EL GENERO DE LOS HOMBRES PARA REALIZAR UNA SERIE DE CALCULOS
        ttlHom=ttlHom+1
        sumAltHom=sumAltHom+alt
        promAltHom=sumAltHom/ttlHom
        sumPesHom=sumPesHom+pes
        promPesHom=sumPesHom/ttlHom
    else:                               #ESTE CONDICIONAL SELECCIONA LAS MUJERES PARA REALIZAR UNA SERIE DE CALCULOS 
         ttlMuj=ttlMuj+1
         sumAltMuj=sumAltMuj+alt
         promAltMuj=sumAltMuj/ttlMuj
         sumPesMuj=sumPesMuj+pes
         promPesMuj=sumPesMuj/ttlMuj

print('NOMBRE --- GENERO --- ALTURA --- PESO')      #IMPRIME EL ENCABEZADO PARA DAR A CONOCER CUALES SON LOS DATOS QUE SE TIENE DE CADA UNA DE LAS PERSONAS

while contador1 <= len (listNom):                   #ESTE CICLO CUMPLE LA FUNCION DE CONTAR Y IMPRIMIR EN EL ORDEN ADECUADO TODOS LOS DATOS QUE SE HAN INGRESADO
    print(listNom[x] + '---' +str (listGen[x]) + '---' +str (listAlt[x]) + '---' +str (listPes[x]))
    x=x+1
    contador1=contador1+1

print('La cantidad de hombres es: '+str(ttlHom))                                #IMPRIME LA CANTIDAD DE HOMBRES QUE SE INGRESARON
print('El promedio de las alturas de los hombres es: ' + str (promAltHom))      #IMPRIME EL PROMEDIO DE LA ALTURA DE LOS HOMBRES
print('El promedio del peso de los hombres es: ' + str (promPesHom))            #IMPRIME EL PROMEDIO DEL PESO DE LOS HOMBRES
print('La cantidad de mujeres es: '+str(ttlMuj))                                #IMPRIME LA CANTIDAD DE MUJERES QUE SE INGRESARON
print('El promedio de las alturas de las mujeres es: ' + str (promAltMuj))      #IMPRIME EL PROMEDIO DE LA ALTURA DE LAS MUJERES
print('El promedio del peso de las mujeres es: ' + str (promPesMuj))            #IMPRIME EL PROMEDIO DEL PESO DE LAS MUJERES
    
