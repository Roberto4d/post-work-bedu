from pago_tarjeta import Tarjeta

class Usuario(Tarjeta):
    def __init__(self, nombre):
        self.nombre = nombre
        self.tarjetas = []

    def lista_tarjetas(self):
        bandera = True
        while bandera:
            capturar = str(input("Desea capturar otra tarjeta? (si/no): "))
            capturar = capturar.upper()
            if capturar == "SI":
                tarjeta = self.crear_tarjeta()
                tarjeta = [self.nombre,self.tasa,self.deuda,self.pago,self.cargo]
                self.captura_nueva_deuda()
                self.tarjetas.append(tarjeta)    
            else:
                bandera = False 
        print(self.tarjetas)

        for t in self.tarjetas:
            self.generar_reporte()
    
    def __str__(self):
        suma = 0 
        for i in range(len(self.tarjetas)):
            print(i)
            suma += 1
        print(f"El usuario: {self.nombre} y tiene {suma} tarjetas")
    
    def __del__(self):
        print(f"Objeto {self.nombre} de clase MiClase destruido")