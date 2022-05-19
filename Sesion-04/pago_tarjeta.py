"""Crea la clase tarjeta de crédito considerando lo siguiente:"""
"""Determina los atributos que debería de tener una tarjeta y asignalos con la función constructor (__init__())
Convierte las funciones del módulo tarjeta a métodos"""

class Tarjeta:
    def __init__(self):
       nombre = input("Ingresa el nombre del titular de la tarjeta: ")
       self.nombre = nombre.title()
       self.tasa =  float(input("Ingresa la tasa de interes: "))
       self.deuda = float(input("Ingresa deuda: "))
       self.pago = float(input("Ingresa pago a realizar: "))
       self.cargo = float(input("Ingresa nuevos cargos: "))
       if self.deuda < self.pago:
            print('No es posible realizar un pago mayor a la deuda!')
            self.__init__()
        
    def captura_nueva_deuda(self):
        deuda_despues_pago = self.deuda - self.pago
        interesMensual = (((self.tasa / 365)*.01) * 30)
        interes_del_mes = round((interesMensual * deuda_despues_pago),2) 
        deuda_recalculada = round ((interes_del_mes + deuda_despues_pago), 2)
        nueva_deuda =  round((self.cargo + deuda_recalculada),2)

        self.deuda_despues_pago = deuda_despues_pago
        self.interes_del_mes = interes_del_mes
        self.deuda_recalculada = deuda_recalculada
        self.nueva_deuda = nueva_deuda

    def generar_reporte(self):   
        print("--------"*6) 
        print("*******"*3 + "Resumen" + "*******"*3)
        print("--------"*6) 
        print("Nombre de la tarjeta: ", self.nombre)
        print("Tasa de interes anual: ", self.tasa , "%")
        print("--------"*6) 
        print("Deuda actual: ", self.deuda, "$")
        print("Monto del Pago: ", self.pago, "$")
        print("--------"*6) 
        print("Deuda despues del pago:", self.deuda_despues_pago)
        print("Interes del Mes:", self.interes_del_mes)
        print("--------"*6) 
        print("Deuda recalculada:", self.deuda_recalculada)
        print("Nuevos Cargos Del Mes: ", self.cargo)
        print("--------"*6) 
        print("Nueva Deuda Del Mes: ", self.nueva_deuda , "$")

    def pago_recurrente(self):
        
        bandera = True
        contador = 0
        while bandera: 
            contador = contador + 1
            if contador == 1:
                self.captura_nueva_deuda()
                self.generar_reporte()   
            elif self.deuda >= self.pago:
                self.deuda = self.nueva_deuda
                self.cargo = 0
                self.captura_nueva_deuda()
                self.generar_reporte()
                self.deuda = self.nueva_deuda
            else:     
                self.pago = self.deuda
                self.captura_nueva_deuda()
                self.generar_reporte()
                bandera = False
        print(contador)

    def multiples_pagos(self):
        pagos = 1
        while pagos != 0 :
            pagos = float(input("Ingresa la cantidad a pagar: "))
            if self.deuda >= self.pago:
                self.cargo = 0
                self.pago = pagos
                self.deuda = self.nueva_deuda    
                self.captura_nueva_deuda()
                self.generar_reporte()








tarjeta1 = Tarjeta()
tarjeta1.captura_nueva_deuda()
tarjeta1.generar_reporte()
# tarjeta1.pago_recurrente()
# tarjeta1.multiples_pagos()