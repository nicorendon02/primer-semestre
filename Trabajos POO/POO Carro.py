# Definir una clase
class carro:
    def __init__(self):
        self.marca = []
        self.placa = []
        self.cc = []
        self.color = []
        self.estado = []
        self.combustible = []

    def capturaDatos(self):
        for i in range(2):
            v_marca = input("Digite la marca del Vehículo: ")
            self.marca.append(v_marca)
            self.placa.append(input("Digite la placa del Vehiculo: "))
            self.cc.append(input("Digite el cilindraje: "))
            self.color.append(input("Digite el color: "))
            self.estado.append("Apagado")
            self.combustible.append(0)

    def imprimirDatos(self):
        for i in range(2):
            print("Marca : " + self.marca[i])
            print("Placa : " + self.placa[i])
            print("Cilindraje : " + self.cc[i])
            print("Color : " + self.color[i])
            print("Estado : " + self.estado[i])
            print("Nivel de Combustible : " + str(self.combustible[i]))
            print("==========================")

    def encenderCarros(self):
        for i in range(2):
            if (self.combustible[i] > 0):
                self.estado[i] = "Encendido"
            else:
                print("El carro: " + self.marca[i] + "Debe tanquear....")

    def tanquearCarro(self, pCarro, pGalones):
        for i in range(2):
            if (self.marca[i] == pCarro):
                self.combustible[i] = self.combustible[i] + pGalones


# ====================================================
# Instancia de la Clase

objCarros = carro()

# Enviar un mensaje para que se ejecuten los métodos

objCarros.capturaDatos()
objCarros.imprimirDatos()

# Invocar al método que enciende los carros
print("ENCENDER LOS CARROS")
objCarros.encenderCarros()
objCarros.imprimirDatos()

# Tanquear un Carro

print("LUEGO DE TANQUEAR EL AUDI")
objCarros.tanquearCarro("AUDI", 10)
objCarros.encenderCarros()
objCarros.imprimirDatos()