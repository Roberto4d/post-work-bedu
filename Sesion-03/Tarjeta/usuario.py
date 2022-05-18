"""Modulo en pyton que implementa un programa para captura multiples datos siguientes:"""

"""Esta funcion te pregunta si quieres capturar una tarjeta y la agrega a una lista de diccionarios.
En caso de que le digas que si y cualquier otra tecla termina la funcion e imprime los reportes de las tarjetas guardadas"""

from tarjeta import crea_tarjeta, captura_nueva_deuda, generar_reporte

def lista_tarjetas():
    bandera = True
    lista_de_tarjetas = []
    while bandera:
        capturar = str(input("Desea capturar otra tarjeta? (si/no): "))
        capturar = capturar.upper()
        if capturar == "SI":
            diccionario = crea_tarjeta()
            captura_nueva_deuda(diccionario)
            lista_de_tarjetas.append(diccionario)    
        else:
            bandera = False 

    for tarjeta in lista_de_tarjetas:
        generar_reporte(tarjeta)
           
lista_tarjetas()