from pago_tarjeta import Tarjeta

class Usuario(Tarjeta):
    def __init__(self, nombres):
        self.nombres = nombres
        self.tarjetas = []

    def lista_tarjetas(self):
        bandera = True
        while bandera:
            capturar = str(input("Desea capturar otra tarjeta? (si/no): "))
            capturar = capturar.upper()
            if capturar == "SI":
                tarjeta = super().__init__()
                self.captura_nueva_deuda()
                tarjeta = [self.nombre,self.tasa,self.deuda,self.pago,self.cargo, self.deuda_despues_pago,self.interes_del_mes,self.deuda_recalculada,self.nueva_deuda]
                self.tarjetas.append(tarjeta) 
                self.generar_reporte()  
            else:
                bandera = False 
        print(self.tarjetas)
  
    def __str__(self):
        suma = 0 
        for t in range(len(self.tarjetas)):
            suma += 1
        print(f"El usuario: {self.nombres} y tiene {suma} tarjetas")
    
    def __del__(self):
        bandera = True
        while bandera:
            numero = int(input("Numero de su tarjeta que desea borrar: "))
            if numero != 0:
                for t in range(len(self.tarjetas)):
                    if numero == t+1:
                        print(f"Objeto {self.nombre} de su tarjeta destruido")
                        self.tarjetas.pop(t)
                        self.generar_reporte()
            else:
                bandera = False
    

            
            
            

        