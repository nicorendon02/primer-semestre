#  Desarrollar una función que reciba el valor en pesos y los convierta a USD

#  RESPUESTA SIN FUNCIÓN
lecPes=0
valDolAct=4040
camDol=0.0

print("CONVERTIR DE PESOS A DOLARE")    
lecPes=int(input("Digite cantidad de pesos Colombianos : "))
camDol=lecPes/valDolAct
print("Ustes recibirá : " + str(camDol))

# RESPUESTA USANDO UNA FUNCIÒN SENCILLA
# Desarrollo de la función
def func_cambio():
    lecPes=0
    valDolAct=4040
    camDol=0.0
    
    print("CONVERTIR DE PESOS A DOLARE")    
    lecPes=int(input("Digite cantidad de pesos Colombianos : "))
    camDol=lecPes/valDolAct
    print("Ustes recibirá : " + str(camDol))

#Llamado de la función
func_cambio()
    
# RESPUESTA CON UNA FUNCIÓN RECIBIENDO PARÁMETRO Y SIN RETORNAR VALOR

def func_cambio(par_lecPes):
    valDolAct=4040
    camDol=0.0
    
    camDol=lecPes/valDolAct
    print("Ustes recibirá : " + str(camDol))

# LEER LOS DATOS PARA ENVIAR A LA FUNCIÓN
print("CONVERTIR DE PESOS A DOLARE")    
lecPes=int(input("Digite cantidad de pesos Colombianos : "))

# HACER EL LLAMADO A LA FUNCIÓN
func_cambio(lecPes)


# RESPUESTA CON UNA FUNCIÓN QUE RECIBE PARAMETRO Y RETORNA VALOR
def func_cambio(par_lecPes):
    valDolAct=4040
    camDol=0.0
    
    camDol=lecPes/valDolAct
    return camDol
# LEER LOS DATOS PARA ENVIAR A LA FUNCIÓN
print("CONVERTIR DE PESOS A DOLARE")    
lecPes=int(input("Digite cantidad de pesos Colombianos : "))

# HACER EL LLAMADO A LA FUNCIÓN
resCam=func_cambio(lecPes)
print("Ustes recibirá : " + str(resCam))

#  PRIMERA FORMA:  FUNCION QUE NO RECIBE NI RETORNA

#=========================================================================
# Esta casa de cambio trabaja con USD y con EUR
#Desarrollar una función para USD y Otra para EUR

#Desarrollo función que convierte de pesos a USD
def func_camPesDol(par_lecPes):
    valDolAct=4040
    camDol=0.0
    camDol=lecPes//valDolAct
    return camDol

#Desarrollo función que convierte de pesos a EUR
def func_camPesEur(par_lecPes):
    valEurAct=4378
    camEur=0.0
    camEur=lecPes//valEurAct
    return camEur

# LEER LOS DATOS PARA ENVIAR A LA FUNCIÓN
print("CASA DE CAMBIO")    
lecPes=int(input("Digite cantidad de pesos Colombianos : "))
tipCam=input("Digite usd para dolar o eur para euro :")

if(tipCam == "usd"):
    print(" Usted recibe en DOLARES : " + str(func_camPesDol(lecPes)))
else:
    if(tipCam == "eur"):
        print(" Usted recibe en EUROS : " + str(func_camPesEur(lecPes)))
    else:
        print("Esa moneda no la CONOCEMOS")
#==========================================================================

#  RESOLVER EL EJERCICIO ANTERIO EN UNA SOLA FUNCIÓN

def func_camPesDoloEur(par_lecPes,par_lecTipMon):
    valDolAct=4040
    valEurAct=4378
    resCam=0.0
    
    if(par_lecTipMon == "usd"):
        resCam=(par_lecPes//valDolAct)
    else:
        if(par_lecTipMon  == "eur"):
            resCam=(par_lecPes//valEurAct)        
        else:
            print("Esa moneda no la CONOCEMOS")
    return resCam            

# LEER LOS DATOS PARA ENVIAR A LA FUNCIÓN
print("CASA DE CAMBIO")    
lecPes=int(input("Digite cantidad de pesos Colombianos : "))
lecTipCam=input("Digite usd para dolar o eur para euro :")

print(" Usted recibe : " + str(func_camPesDoloEur(lecPes,lecTipCam)))
