#Ejercicio Herencia - Formas geométricas
#declarar super clase

class forma:
    def __init__(self):
        self.color = input('Digite el color de la figura: ')

    def imprimir(self):
        print('Color de la figura: ' + self.color)

#declarar sub clases...
#================================

class cuadrado(forma):
    def __init__(self):
        super().__init__()
        self.lado = int(input('Digite valor del lado del cuadrado: '))
        self.areaCuad = (self.lado**2)

    def imprimirHerCuad(self):
        super().imprimir()
        print('Lado del cuadrado: ' + str(self.lado))
        print('Area del cuadrado: ' + str(self.areaCuad))

class rectangulo(forma):
    def __init__(self):
        super().__init__()
        self.base = int(input('Digite la base del rectángulo: '))
        self.altura = int(input('Digite la altura del rectángulo: '))
        self.areaRec = ((self.base)*(self.altura))

    def imprimirHerRec(self):
        super().imprimir()
        print('Base: ' + str(self.base))
        print('Altura: ' + str(self.altura))
        print('Area del rectángulo: ' + str(self.areaRec))

class circulo(forma):
    def __init__(self):
        super().__init__()
        self.radio = int(input('Digite radio del círculo: '))
        self.areaCir = ((3.1416)*(self.radio**2))

    def imprimirHerCir(self):
        super().imprimir()
        print('π: 3.1416')
        print('Radio: ' + str(self.radio))
        print('Area del circulo: ' + str(self.areaCir))

#generar instancias....
#================================

print('==============')
print('OBJETO CUADRADO')
obj_cuad = cuadrado()

print('==============')
print('OBJETO RECTANGULO')
obj_rec = rectangulo()

print('==============')
print('OBJETO CIRCULO')
obj_cir = circulo()

#================================
print('==============')
print('IMPRESIONES CUADRADO')
obj_cuad.imprimirHerCuad()

print('==============')
print('IMPRESIONES RECTANGULO')
obj_rec.imprimirHerRec()

print('==============')
print('IMPRESIONES CIRCULO')
obj_cir.imprimirHerCir()

#fin del programa.

