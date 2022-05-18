"""Importacion desde el paquete Tarjeta"""
from Tarjeta.tarjeta import crea_tarjeta, captura_nueva_deuda, generar_reporte, pago_recurrente, multiples_pagos

diccionario = crea_tarjeta()
diccionario = captura_nueva_deuda(diccionario)
generar_reporte(diccionario)

pago_recurrente()

multiples_pagos()

