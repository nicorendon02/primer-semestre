# Herencia

# Declarar la clase principal

class CPersona:
    # Método constructor
    def __init__(self):
        # Declarar los atributos de la clase
        self.nombre = input("Digite el Nombre : ")
        self.apellido = input("Digite el Apellido : ")
        self.edad = input("Digite la Edad : ")

    # Método que imprime los datos almacenados en los atributos
    def imprimir(self):
        print("Nombre : " + self.nombre)
        print("Apellido : " + self.apellido)
        print('Edad: '+ self.edad)


#  Declara la subclase o clase heredada

class CEstudiante(CPersona):
    # Metodos de la clase - constructor - Parámetros
    def __init__(self):
        # Declarar los atributos de la clase
        print("CAPTURA DATOS DEL ESTUDIANTE")
        super().__init__()  # Llamado a la clase principal
        self.codigo = input("Digite Codigo del Estudiante : ")
        self.carrera = input("Digite la carrera del Estudiante : ")
        self.semestre = input("Semestre que cursa el Estudiante : ")

    def imprimirHer(self):
        print("IMPRIME EL ESTUDIANTE")
        super().imprimir()
        print("Codigo : " + self.codigo)
        print("Carrera : " + self.carrera)
        print('Semestre: '+ self.semestre)

    # Declarar otra subclase


class CProfesor(CPersona):
    # Metodos de la clase - constructor - Parámetros
    def __init__(self):
        print("CAPTURA DATOS DEL PROFESOR")
        # Declarar los atributos de la clase
        super().__init__()  # Llamado a la clase principal
        self.profesion = input("Digite Profesion del Profesor : ")
        self.facultad = input("Digite Facultad del Profesor : ")
        self.asignatura = input("Digite asignatura que imparte el Profesor : ")

    def imprimirHer(self):
        print("IMPRIME EL PROFESOR")
        super().imprimir()
        print("Profesión del Profesor : " + self.profesion)
        print("Facultad del Profesor : " + self.facultad)
        print('Asignatura que imparte: '+ self.asignatura)


class CAdministrativo(CPersona):
    def __init__(self):
        print("CAPTURA DATOS DEL ADMINISTRATIVO")
        # Declarar los atributos de la clase
        super().__init__()  # Llamado a la clase principal
        self.cargo = input("Digite cargo del Administrativo : ")

    def imprimirHer(self):
        print("IMPRIME EL ADMINISTRATIVO")
        super().imprimir()
        print("Cargo del Administrativo : " + self.cargo)

    #  Principal

'''
#  Generar Instancias de la Clase Principal   

print("====  CONSTRUIR EL OBJETO Y MEDIR LOS DATAS =====")
obj_PersonaUno = CPersona()
obj_PersonaDos = CPersona()  

#  Enviar mensaje para que se ejecute el método imprimir
print("====  IMPRIMIR EL OBJETO PERSONAUNO =====")
obj_PersonaUno.imprimir()

print("====  IMPRIMIR EL OBJETO PERSONADOS =====")
obj_PersonaDos.imprimir()
'''

#  Generar Instancias de la Clase Derivada

objUno_HerEstUno = CEstudiante()
objDos_HerProUno = CProfesor()
objTres_HerAdmUno = CAdministrativo()

# Imprimir el objeto Heredado
objUno_HerEstUno.imprimirHer()
objDos_HerProUno.imprimirHer()
objTres_HerAdmUno.imprimirHer()