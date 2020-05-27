lista=["nico","m",3.8,4.2,3,20]
defi=(lista[2]+lista[3]+lista[4])//3
if lista[5]>=12:
    defi=defi//2
    print('pierde por INASISTENCIAS con la def: '+str(defi))
else:
    if defi<3:
        print('pierde ACADEMICAMENTE con la def: '+str(defi))
    else:
        print('gano ACADEMICAMENTE con la def: '+str(defi))
