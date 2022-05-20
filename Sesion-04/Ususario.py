from pago_tarjeta import Tarjeta

class Usuario(Tarjeta):
    def __init__(self, nombre):
        self.nombre = nombre
        self.tarjetas = []

    def agregar_tarjeta(self):
        tar = super().__init__()
        tar = self.captura_nueva_deuda()
        self.tarjetas.append(tar)
    
    def imprimir_lista(self):
        for tarjeta in self.tarjetas:
            self.generar_reporte(tarjeta)
        
  
    def __str__(self):
        suma = 0 
        for t in range(len(self.tarjetas)):
            suma += 1
        print(f"El usuario: {self.nombre} y tiene {suma} tarjetas")
    
    def __del__(self):
        lista = self.tarjetas
        numero = int(input("Numero de su tarjeta que desea borrar: "))
        for t in range(len(lista)):
            if numero == t+1:
                print(f"Objeto {self.nombre} de su tarjeta destruido")
                lista.pop(t)
        return lista


    # def lista_tarjetas(self):
    #     bandera = True
    #     while bandera:
    #         capturar = str(input("Desea capturar otra tarjeta? (si/no): "))
    #         capturar = capturar.upper()
    #         if capturar == "SI":
    #             tarjeta = super().__init__()
    #             self.captura_nueva_deuda()
    #             tarjeta = [self.nombre,self.tasa,self.deuda,self.pago,self.cargo, self.deuda_despues_pago,self.interes_del_mes,self.deuda_recalculada,self.nueva_deuda]
    #             self.tarjetas.append(tarjeta) 
    #         else:
    #             bandera = False 
    #     return self.tarjetas

    # def __del__(self):
    #     lista = self.tarjetas
    #     print(lista)
    #     bandera = True
    #     while bandera:
    #         numero = int(input("Numero de su tarjeta que desea borrar: "))
    #         if numero != 0:
    #             for t in range(len(lista)):
    #                 if numero == t+1:
    #                     print(f"Objeto {self.nombre} de su tarjeta destruido")
    #                     lista.pop(t)
    #             return lista
    #         else:
    #             bandera = False

        
            
            
 
        