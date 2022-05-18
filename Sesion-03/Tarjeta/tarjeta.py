"""Modulo en pyton que implementa un programa para captura multiples datos y generar algunos calculos siguientes:"""
"""Esta funcion contiene la captura de datos de una tarjeta, y devuelve un diccionario con la informacion 
capturada, y marca un error en el caso de que se ingrese un monto mayor de pago del posible"""

def crea_tarjeta():
    nombre = input("Ingresa el nombre del titular de la tarjeta: ")
    tasa   = float(input("Ingresa la tasa de interes: "))
    deuda  = float(input("Ingresa deuda: "))
    pago   = float(input("Ingresa pago a realizar: "))
    cargo  = float(input("Ingresa nuevos cargos: ")) 
   
    if deuda < pago:
        print('No es posible realizar un pago mayor a la deuda!')
        return crea_tarjeta()
    else:
        diccionario = {"NombreTarjeta": nombre, "Tasa": tasa, "Deuda": deuda, "Pago": pago, "Cargo": cargo}
       
    return diccionario

   
"""Esa funcion recibe un diccionario con los datos de la tarjeta, genera los calculos y agrega la nueva deuda como
un dato al diccionario"""

def captura_nueva_deuda(diccionario):
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
    
    return diccionario
  
"""Esta funcion recibe un diccionario con la informacion de una tarjeta e imprime el reporte """

def generar_reporte(diccionario):   
    print("--------"*6) 
    print("*******"*3 + "Resumen" + "*******"*3)
    print("--------"*6) 
    print("Nombre de la tarjeta: ", diccionario["NombreTarjeta"])
    print("Tasa de interes anual: ", diccionario["Tasa"] , "%")
    print("--------"*6) 
    print("Deuda actual: ", diccionario["Deuda"], "$")
    print("Monto del Pago: ", diccionario["Pago"], "$")
    print("--------"*6) 
    print("Deuda despues del pago:", diccionario["Deuda_Despues_De_Pago"])
    print("Interes del Mes:", diccionario["Interes_Del_Mes"])
    print("--------"*6) 
    print("Deuda recalculada:", diccionario["Deuda_Recalculada"])
    print("Nuevos Cargos Del Mes: ", diccionario["Cargo"])
    print("--------"*6) 
    print("Nueva Deuda Del Mes: ",diccionario["Nueva_Deuda"], "$")

  
"""   Esta funcion, recibe un diccionario con los datos de una tarjeta. 
Proyecta una serie de pagos del mismo monto en una tarjeta hasta convertir el valor de la deuda en 0
Considera que no habrá nuevos cargos. Para ca da mes proyectado se imprime el reporte correspondiente."""

def pago_recurrente():
    diccionario = crea_tarjeta()
    bandera = True
    contador = 0 
    while bandera:
        contador = contador + 1
        if contador == 1:
            captura_nueva_deuda(diccionario)
            generar_reporte(diccionario) 
        elif diccionario["Deuda"] >= diccionario["Pago"]:
            diccionario["Deuda"] = diccionario["Nueva_Deuda"]
            diccionario["Cargo"] = 0
            captura_nueva_deuda(diccionario)
            generar_reporte(diccionario)
            diccionario["Deuda"] = diccionario["Nueva_Deuda"]
        else:     
            diccionario["Pago"] = diccionario["Deuda"]
            captura_nueva_deuda(diccionario)
            generar_reporte(diccionario)
            bandera = False
        
pago_recurrente()   

"""Esta función proyecta multiples pagos distintos sobre una tarjeta a traves de los meses, pide la cantidad a pagar e imprime el reporte"""

def multiples_pagos():
    diccionario = crea_tarjeta()
    diccionario1 = captura_nueva_deuda(diccionario)
    generar_reporte(diccionario1)
    pagos = 1
    while pagos != 0 :
        pagos = float(input("Ingresa la cantidad a pagar: "))
        if diccionario["Deuda"] >= diccionario["Pago"]:
            diccionario["Cargo"] = 0
            diccionario["Pago"] = pagos
            diccionario["Deuda"] = diccionario["Nueva_Deuda"]    
            diccionario1 = captura_nueva_deuda(diccionario)
            generar_reporte(diccionario1)

multiples_pagos()
