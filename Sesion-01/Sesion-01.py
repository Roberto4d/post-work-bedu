
"""Solicita al usuario los siguientes datos"""

nombre = input("Ingresa el nombre de la tarjeta: ")
tasa   = float(input("Ingresa la tasa de interes: "))
deuda  = int(input("Ingresa deuda: "))
pago   = int(input("Ingresa pago a realizar: "))
cargo  = int(input("Ingresa nuevos cargos: "))

def deudaDespuesPago():
    return deuda - pago
def interesDelMes():
    interesMensual = (((tasa / 365)*.01) * 30)
    return ( interesMensual * deudaDespuesPago() )
def  deudaRecalculada():
    return interesDelMes() + deudaDespuesPago() 
def nuevaDeuda():
    return cargo + deudaRecalculada()    

print("******"*3 + "Resumen" + "******"*3)
print("Nombre de la tarjeta: ", nombre)
print("Tasa de interes anual: ", tasa , "%")
print("******"*3 + "Resumen" + "******"*3)
print("Deuda actual: ", deuda, "$")
print("Monto del Pago: ", pago, "$")
print("******"*3 + "Resumen" + "******"*3)
print("Deuda despues del pago:", deudaDespuesPago())
print("Interes del Mes:", interesDelMes())
print("******"*3 + "Resumen" + "******"*3)
print("Deuda recalculada:", deudaRecalculada())
print("Nuevos Cargos Del Mes: ", cargo, "$")
print("******"*3 + "Resumen" + "******"*3)
print("Nueva Deuda Del Mes: ",nuevaDeuda(), "$")






