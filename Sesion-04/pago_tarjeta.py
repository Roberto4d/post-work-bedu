"""Crea la clase tarjeta de crédito considerando lo siguiente:"""
"""Determina los atributos que debería de tener una tarjeta y asignalos con la función constructor (__init__())
Convierte las funciones del módulo tarjeta a métodos"""

class Tarjeta:
    def __init__(self, nombre, tasa, deuda, pago, cargo):
        self.nombre = nombre
        self.tasa = tasa
        self.deuda = deuda
        self.pago = pago
        self.cargo = cargo
    def crea_tarjeta(self):
        self.nombre = input("Ingresa el nombre del titular de la tarjeta: ")
        self.tasa   = float(input("Ingresa la tasa de interes: "))
        self.deuda  = float(input("Ingresa deuda: "))
        self.pago   = float(input("Ingresa pago a realizar: "))
        self.cargo  = float(input("Ingresa nuevos cargos: ")) 
        if self.deuda < self.pago:
            print('No es posible realizar un pago mayor a la deuda!')
            return self.crea_tarjeta()
        else:
            diccionario = {"NombreTarjeta": self.nombre, "Tasa": self.tasa, "Deuda": self.deuda, "Pago": self.pago, "Cargo": self.cargo}
        return diccionario
    def captura_nueva_deuda(self, diccionario):
        deuda_despues_pago = diccionario["Deuda"] - diccionario["Pago"]
        interesMensual = (((diccionario["Tasa"] / 365)*.01) * 30)
        interes_del_mes = interesMensual * deuda_despues_pago 
        interes_del_mes = round(interes_del_mes,2)
        deuda_recalculada = interes_del_mes + deuda_despues_pago
        deuda_recalculada = round(deuda_recalculada,2)
        nueva_deuda =  diccionario["Cargo"] + deuda_recalculada
        nueva_deuda = round(nueva_deuda,2)    
        
        diccionario["Deuda_Despues_De_Pago"] = deuda_despues_pago
        diccionario["Interes_Del_Mes"] = interes_del_mes
        diccionario["Deuda_Recalculada"] = deuda_recalculada
        diccionario["Nueva_Deuda"] = nueva_deuda

cliente1 = Tarjeta("Roberto", 33, 1000, 550, 100)
# cliente2 = Tarjeta("Jenn", 25, 5000, 2500, 500)

# print(type(cliente1))
# print(type(cliente2 ))

# print(cliente1.nombre, cliente1.deuda)
# print(cliente2.nombre, cliente2.deuda)
cliente1.crea_tarjeta()
cliente1.captura_nueva_deuda()