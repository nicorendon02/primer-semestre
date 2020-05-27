#declaracion/prototipo de la funcion
def func_imprimirDatosPersonales():
    print('IMPRESION DE DATOS DIRECTOS')
    print('Codigo: 82202014240')
    print('Nombre: Nicolas')
    print('Apellidos: Rendon Arias')
    print('Genero: M')
    print('Edad: 17')

def func_espacio():
    print('------------------------------------------------------')

def func_imprimirDatosPersonalesVarLoc():
    print('IMPRESION CON VARIABLES LOCALES')
    cod="82202014240"
    nom="Nicolas"
    ape="Rendon Arias"
    gen="M"
    edd="17"
    print('Codigo: '+cod+' '+'Nombre: '+str(nom)+' '+'Apellidos: '+str(ape)+' '+'Genero: '+str(gen)+' '+'Edad: '+edd)

#llamar/invocar la funcion desarrollada
func_imprimirDatosPersonales()
func_espacio()
func_imprimirDatosPersonalesVarLoc()
