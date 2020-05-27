canEst=2
canMat=2
x=0
canMat=2
conCic=0
conMat=0
lisPar=[]
canHom=[]
canMuj=[]
promHom=[]
promMuj=[]

print('PRUEBA PARA 2 ESTUDIANTES Y 2 MATERIAS')
while conCic<canEst:
    
    nom=input('ingrese el nombre: ')
    gen=input('ingrese genero: ')
    numMat=1
    for x in range (canMat):
        print('MATERIA '+str(numMat))
        par1=float(input('ingrese la nota del primer parcial: '))
        lisPar.append(par1)
        par2=float(input('ingrese la nota del segundo parcial: '))
        lisPar.append(par2)
        par3=float(input('ingrese la nota del tercer parcial: '))
        lisPar.append(par3)

        ina=int(input('ingrese la cantidad de inasistencias: '))
   
        prom=(sum(lisPar))/3
        numMat=numMat+1

        if prom<3:
            print(str(nom)+' pierde ACADEMICAMENTE con el promedio: '+str(prom))
        else:
            print(str(nom)+' gano ACADEMICAMENTE con el promedio: '+str(prom))
        if ina>=12:
            prom=prom/2
            print(str(nom)+' pierde POR INASISTENCIAS con un promedio de: '+str(prom))

        if gen.casefold()=='M'.casefold():
            canHom.append(nom)
            promHom.append(prom)
        else:
            canMuj.append(nom)
            promMuj.append(prom)
              
    conCic=conCic+1
defiHom=(sum(promHom)/canMat)
defiMuj=(sum(promMuj)/canMat)
print('la definitiva de '+str(canHom)+' es: '+str(defiHom))
print('la definitiva de '+str(canMuj)+' es: '+str(defiMuj))
    
