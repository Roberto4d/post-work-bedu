from pago_tarjeta import Tarjeta


class Tarjeta_de_servicios(Tarjeta):
    def __init__(self):
        super(Tarjeta_de_servicios,self).__init__
        nombre = input("Nombre de la tarjeta: ")
        self.nombre = nombre.title()
        self.deuda = float(input("Escribe el monto de la deuda actual de la tarjeta: "))
        self.pago = 0
        self.cargo = float(input("Ingresa nuevos cargos: "))
        self.deuda__recalculada = self.deuda - self.pago
        self.nueva_deuda = self.deuda__recalculada + self.cargo
    
    def calculos(self):
        self.pago = float(input("Escribe el monto del pago a realizar (sólo se hacepta un pago igual a la deuda):"))
        if self.pago == self.deuda:
            self.deuda__recalculada = self.deuda - self.pago
            self.nueva_deuda = self.deuda__recalculada + self.cargo
            self.reporte()
        else:
            print("Sólo es posible realizar un pago igual a la deuda actual!")
            self.calculos()

    def reporte(self):
        print("---------"*6)
        print("*******"*3 + "Tarjeta de Servisios" + "*******"*3)
        print("---------"*6)
        print("Nombre de la tarjeta: ", self.nombre)
        print("---------"*6)
        print("Deuda actual: ", self.deuda, "$")
        print("Monto del Pago: ", self.pago, "$")
        print("---------"*6)
        print("Deuda despues del pago:", self.deuda__recalculada)
        print("Nuevos Cargos Del Mes: ", self.cargo)
        print("---------"*6)
        print("Nueva Deuda Del Mes: ", self.nueva_deuda , "$")
        print("---------"*6)



tarjeta_servicios = Tarjeta_de_servicios()
tarjeta_servicios.reporte()
tarjeta_servicios.calculos()
