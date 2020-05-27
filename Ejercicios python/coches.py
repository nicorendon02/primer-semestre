class coche():

    def __init__(self):
        self.largoChasis=250
        self.anchoChasis=120
        self.__ruedas=4
        self.marca='renault'
        self.tipoCombustible='diesel'
        self.nivelCombustible=100
        self.aceleracion=0
        self.enmarcha=False

    def arrancar(self, arrancamos):
        self.enmarcha=arrancamos

        if (self.enmarcha):
            return 'El carro está en marcha'
        else:
            return 'El carro está en reposo'

    def estado(self):
        print('')

#en ejecución...