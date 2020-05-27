lisNom=[]
lisGen=[]
lisAlt=[]
lisPes=[]

lisAltHom=[]
lisAltMuj=[]

lisPesHom=[]
lisPesMuj=[]

lisHom=[]
lisMuj=[]

mayAltMas=0
menAltMas=5

mayPesMas=0
menPesMas=1000

mayAltFem=0
menAltFem=5

mayPesFem=0
menPesFem=1000

homMasAlt=''
homMasBaj=''

mujMasAlt=''
mujMasBaj=''

homMasPes=''
homMenPes=''

mujMasPes=''
mujMenPes=''

homRiesCar=[]
mujRiesCar=[]

canPer=int(input('ingrese la cantidad de personas: '))
for x in range (canPer):
    nom=input('ingrese su nombre: ')
    lisNom.append(nom)
    gen=input('ingrese su genero (M para masculino o F para femenino): ')
    lisGen.append(gen)
    alt=float(input('ingrese su altura: '))
    lisAlt.append(alt)
    pes=int(input('ingrese su peso: '))
    lisPes.append(pes)

    if gen.casefold()=='m'.casefold():
        lisAltHom.append(alt)
        lisPesHom.append(pes)
        lisHom.append(nom)
        if alt>mayAltMas:
            mayAltMas=alt
            homMasAlt=nom
        else:
            menAltMas=alt
            homMasBaj=nom
            
        if pes>mayPesMas:
            mayPesMas=pes
        else:
            menPesMas=pes
            homMenPes=nom
        if alt<1.6 and pes>80:
            print('Tiene riesgo cardiovascular')
            homRiesCar.append(nom)
    else:
        lisAltMuj.append(alt)
        lisPesMuj.append(pes)
        lisMuj.append(nom)
        if alt>mayAltFem:
            mayAltFem=alt
            mujMasAlt=nom
        else:
            menAltFem=alt
            mujMasBaj=nom
            
        if pes>mayPesFem:
            mayPesFem=pes
        else:
            menPesFem=pes
            mujMenPes=nom
        if alt<1.4 and pes>70:
            print('Tiene riesgo cardiovascular')
            mujRiesCar.append(nom)


promAltHom=(sum(lisAltHom))/len(lisHom)
promAltMuj=(sum(lisAltMuj))/len(lisMuj)
promPesHom=(sum(lisPesHom))/len(lisHom)
promPesMuj=(sum(lisPesHom))/len(lisMuj)

promAltGen=(sum(lisAlt))/len(lisAlt)
promPesGen=(sum(lisPes))/len(lisPes)

print('NOM --- GEN --- ALT --- PES')
for x in range (len(lisNom)):
    print(lisNom[x],lisGen[x],lisAlt[x],lisPes[x],sep="\t")

print('Los hombres son: '+str(lisHom))
print('Las mujeres son: '+str(lisMuj))
print('Promedio altura general: '+str(promAltGen))
print('Promedio peso general: '+str(promPesGen))
print('Hombre más alto: '+ str(homMasAlt)+'con la altura: '+str(mayAltMas))
print('Hombre más bajo: '+ str(homMasBaj)+'con la altura: '+str(menAltMas))
print('Promedio alturas homres: '+str(promAltHom))
print('Mujer más alto: '+ str(mujMasAlt)+'con la altura: '+str(mayAltFem))
print('Mujer más bajo: '+ str(mujMasBaj)+'con la altura: '+str(menAltFem))
print('Promedio alturas mujeres: '+str(promAltMuj))
print('Hombre más pesado: '+ str(homMasPes)+'con el peso: '+str(mayPesMas))
print('Hombre menos pesado: '+ str(homMenPes)+'con el peso: '+str(menPesMas))
print('Promedio pesos homres: '+str(promPesHom))
print('Mujer más pesada: '+ str(mujMasPes)+'con la altura: '+str(mayPesFem))
print('Mujer menos pesada: '+ str(mujMenPes)+'con la altura: '+str(menPesFem))
print('Promedio pesos mujeres: '+str(promPesMuj))
print('Los hombres con riesgo cardiovascular son: '+str(homRiesCar))
print('Las mujeres con riesgo cardiovascular son: '+str(mujRiesCar))
totRiesCar=(len(homRiesCar)+len(mujRiesCar))
print('Total de personas con riesgo cardiovascular: '+str(totRiesCar))



