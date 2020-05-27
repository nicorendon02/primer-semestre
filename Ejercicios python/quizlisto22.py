"""hecho por NICOLAS RENDON ARIAS"""
"""area de definicion de variables"""
conCic=0  #contador del ciclo
conMat=1    #contador de materias
canPer=0    #cantidad de estudiantes o personas

nom=""     #nombre
genEst=""   #contador del genero

maxNotMat=0 #maxima nota de la materia
minNotMat=5 #minima nota de la materia
defMat=0    #definitiva de la materia
defTot=0    #definitiva total

maxNotHom=0 #maxima nota de hombres
minNotHom=5 #minima nota de hombres

maxNotMuj=0 #maxima nota de mujeres
minNotMuj=5 #minima nota de mujeres
nomMinNotHom="" #nombre del hombre con la menor nota
nomMinNotMuj="" #nombre de la mujer con la menor nota
nomMaxNotHom="" #nombre del hombre con la mayor nota
nomMaxNotMuj="" #nombre de la mujer con la mayor nota
canPer=int(input('ingrese la cantidad de estudiantes: '))       #se ingresa la cantidad de estudiantes
canMat=int(input('ingrese la cantidad de materias: '))          #se ingresa la cantidad de materias

"""aqui se ejecuta un ciclo mientras sea menor o igual a cantidad de estudiantes"""
while (conCic<canPer):                                          #mientras el contador del ciclo sea menor a la cantidad de estudiantes

    nom=input('ingrese el nombre del estudiante: ') #se ingresa el nombre
    genEst=input('ingrese el genero: ')  #se ingresa el genero
    numMat=1                                                    #nombre de la materia
    for x in range (canMat):                                    #mientras la variable sea menor o igual a la cantidad de materias
        print('materia '+str(numMat))                               #imprimir el nombre de la materia
        
        par1=float(input('ingrese la nota del primer parcial: ')) #se ingresa la nota del primer parcial
        par2=float(input('ingrese la nota del segundo parcial: ')) #se ingresa la nota del segundo parcial
        par3=float(input('ingrese la nota del tercer parcial: '))  #se ingresa la nota del tercer parcial
        ina=int(input('ingrese la cantidad de inasistencias: '))   #se ingresa la cantidad de inasistencias
        defi=(par1+par2+par3)/3                           #se calcula la operacion para la definitiva de la materia
        numMat=numMat+1                                 #se incrementa el contador de la materia en uno
        
        if (ina>=12):                                       #si la cantidad de inasistencias es mayor o igual a 12
            defi=defi/2                                       #se divide la definitiva entre 2
            print('pierde POR INASISTENCIA con la definitiva: '+str(defi)) #se imprime un aviso que dice que pierde la materia por inasistencias
        else:                                                   #sino
            if (defi>=3):                                  #si la definitiva es mayor o igual a 3
                print('gano ACADEMICAMENTE con una definitiva de: '  +str(defi)) #se imprime un aviso que dice que gano academicamente y la def
            else:                                                  #sino
                print('perdio ACADEMICAMENTE con una definitiva de: '+str(defi)) #se imprime un aviso que dice que perdio academicamente y la def


        if genEst.casefold()=="M".casefold():   #si el genero ingresado es masculino
            
            if defi>maxNotHom:                 #si la definitiva es mayor a la maxima nota masculina
                maxNotHom=defi                 #la maxima nota masculina sera igual a la def
                nomMaxNotHom=nom              #el nombre del hombre con la mayor nota sera igual a nombre
        else:                                   #sino
            if defi<minNotHom:                  #si la def es menor a la minima nota masculina
                minNotHom=defi                   #la minima nota masculina sera igual a la def
                nomMinNotHom=nom                #el nombre del hombre con la menor nota sera igual a nombre

        if genEst.casefold()=="F".casefold():   #si el genero ingresado es femenino
            
            if defi>maxNotMuj:                  #si la def es mayor a la maxima nota femenina
                maxNotMuj=defi                  #la maxima nota femenina sera igual a la def
                nomMaxNotMuj=nom                #el nombre de la mujer con la mayor nota sera igual a nombre
        else:                                  #sino
            if defi<minNotMuj:                 #si la def es menor a la menor nota femenina
                minNotMuj=defi                 #la menor nota femenina sera igual a la defi
                nomMinNotMuj=nom               #el nombre de la mujer con la menor nota sera igual a nombre
        conMat=conMat+1                        #incremento del contador de materias en 1
    conCic=conCic+1                            #incremento del contador del ciclo en 1

"""cierre del ciclo"""    
defTot=defTot+defi                       #acumulador de la def de la materia para sacar la definitiva total
defTotTot=defTot/canMat                  #formula para conseguir la definitiva total del estudiante
print('La definitiva total del estudiante es: '+str(defTotTot)) #se imprime la definitiva total del estudiante

print("La mayor nota de "+str(nomMaxNotHom)+" hasta el momento: "+str(maxNotHom)) #se imprime la mayor nota del hombre
print("La menor nota de "+str(nomMinNotHom)+" hasta el momento: "+str(minNotHom)) #se imprime la menor nota del hombre
print("La mayor nota de "+str(nomMaxNotMuj)+" hasta el momento: "+str(maxNotMuj)) #se imprime la mayor nota de la mujer
print("La menor nota de "+str(nomMinNotMuj)+" hasta el momento: "+str(minNotMuj)) #se imprime la menor nota de la mujer
#end
    
    


