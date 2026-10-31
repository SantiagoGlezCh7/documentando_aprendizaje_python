# ------------------------------------------------------------
# PASO 1 · Datos del equipo
# Pide con input() el nombre del equipo, la cantidad de participantes (int)
# y el presupuesto para snacks por persona (float).
# ------------------------------------------------------------
nombre_equipo = (input("Ingres el nombre del equipo: "))
cant_participantes = int(input("Ingrese la cantidad de participantes: "))
presupuesto_snacks = float(input("Ingres el prespuesto por persona snacks: "))

# ------------------------------------------------------------
# PASO 2 · Tipos de datos
# Muestra con type() el tipo de dato de la cantidad de participantes
# y del presupuesto por persona.
# ------------------------------------------------------------

print(type(nombre_equipo))
print(type(cant_participantes))
print(type(presupuesto_snacks))

# ------------------------------------------------------------
# PASO 3 · Suministros
# Cada participante consumirá 2.5 litros de agua. Calcula los litros totales
# necesarios. Calcula el costo total de los snacks (participantes * presupuesto).
# Redondea el costo total a 2 decimales con round().
# ------------------------------------------------------------
# calcular litos totales necesarios
litros_totales=round(((cant_participantes*2.5)/1),2)
print(litros_totales)

# calcular costos snacks
total_snacks=round(cant_participantes*presupuesto_snacks,2)

print(total_snacks)

#
# ------------------------------------------------------------
# PASO 4 · Duración del evento
# El hackathon dura exactamente 2500 minutos.
# Exprésalo en horas y minutos usando división entera (//) y módulo (%).
# ------------------------------------------------------------

minutos=2500
minutos=int(minutos)
duracio_horas = ((1*minutos)//60)
print(duracio_horas)


duracion_minutos= ((1*minutos)%60)
print(duracion_minutos)
# ------------------------------------------------------------
# PASO 5 · Cuentas extra
# Si el equipo gana un premio de 15000 pesos, calcula cuánto le tocaría
# a cada participante. Además, calcula cuánto costaría el presupuesto de snacks
# por persona si los precios subieran un 8% en 2 años (presupuesto * 1.08 ** 2).
# Redondea ambos resultados a 2 decimales.
# ------------------------------------------------------------
premio=15000
premio=int(premio)

calculo_premio=premio/cant_participantes
print(calculo_premio)
#calculo presupuesto snacks
calculo_presupuesto_snacks=round((presupuesto_snacks*(1.08**2)),2)
print(calculo_presupuesto_snacks)


# ------------------------------------------------------------
# PASO 6 · Resumen
# Muestra un resumen del evento con f-strings, con al menos una línea
# hecha con format(). (Ej: Equipo, Litros totales, Costo snacks,
# Duración en horas y mins, Premio por persona, Costo futuro).
# ------------------------------------------------------------

print(f"Equipo: {nombre_equipo}")
print("Cant de participantes: {}".format(cant_participantes))
print(f"Presupuesto snacks  : {presupuesto_snacks}")
print(f"Calculo litos totales por participantes en total : {litros_totales}")
print(f"Calculo de total de compra de los snacks para el hackaton: {total_snacks}")
print(f"Cuanto le toca a cada quien del premio a los participantes: {calculo_premio}")
print("Duracion total del evento {} horas y {} minutos".format(duracio_horas,duracion_minutos))