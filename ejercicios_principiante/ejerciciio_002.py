# ------------------------------------------------------------
# PASO 1 · Datos del proyecto
# Pide el nombre del color de pintura, los metros cuadrados a pintar (int)
# y el precio de un bote de pintura (float).
# ------------------------------------------------------------
nombre_pintura = (input("escribe el nombre de la pintura: "))
metros_cuadrados_pintar = (input("escribe metros cuadrados a pintar: "))
metros_cuadrados_pintar = int(metros_cuadrados_pintar)
precio_botepintura=(input("escribe precio de pintura: "))
precio_botepintura = float(precio_botepintura)

# ------------------------------------------------------------
# PASO 2 · Tipos de datos
# Muestra el tipo de dato de los metros cuadrados y del precio.
# ------------------------------------------------------------

print(type(nombre_pintura))
print(type(metros_cuadrados_pintar))
print(type(precio_botepintura))
# ------------------------------------------------------------
# PASO 3 · Pintura necesaria
# Un bote de pintura rinde para 10 metros cuadrados. Calcula cuántos botes
# necesitas (metros / 10). Calcula el costo total (botes necesarios * precio).
# Redondea el costo total a 2 decimales.
# ------------------------------------------------------------

calculo_botesnecesito=round((1*metros_cuadrados_pintar)/10,2)
print(calculo_botesnecesito)

costo_total=round(calculo_botesnecesito*precio_botepintura,2)
print(costo_total)

# ------------------------------------------------------------
# PASO 4 · Tiempo de trabajo
# Pintar toma 45 minutos por cada bote utilizado. Calcula el total de minutos
# y luego exprésalo en horas y minutos usando // y %.
# ------------------------------------------------------------


total_minutos = calculo_botesnecesito * 45/1

horas = total_minutos*1//60
print(horas)
minutos=total_minutos*1%60
print(minutos)

# ------------------------------------------------------------
# PASO 5 · Cuentas extra
# Si consigues a 2 ayudantes (3 personas en total), ¿cuántos metros cuadrados
# pintaría cada uno en promedio? Además, calcula el costo total de la pintura
# agregándole el 16% de IVA (costo total * 1.16). Redondea a 2 decimales.
# ------------------------------------------------------------

metros_por_persona = round(metros_cuadrados_pintar/3,2)
print(metros_por_persona)

calculo_totalpintura_iva = round(costo_total * 1.16,2)
print(calculo_totalpintura_iva)




# ------------------------------------------------------------
# PASO 6 · Resumen
# Imprime el resumen usando f-strings y al menos una línea con format().
# ------------------------------------------------------------

print(f"Nombre pintura: {nombre_pintura}")
print("Metros cuadrados a pintar : {}".format(metros_cuadrados_pintar))
print(f"Precio bote pintura  : {precio_botepintura}")
print(f"Calculo de botes que se necesitan para 10 metros cuadrados   : {calculo_botesnecesito}")
print(f"Calculo total de botes de pintura necesaria para 10 metros cuadrados por el precio de los botes  : {costo_total}")
print(f"cuantos metros cuadrados pintaria cada uno en pormedio son 3 personas en total: {metros_por_persona}")
print(f"Caklculo de pintura con IVA 16%: {calculo_totalpintura_iva}")
print("Tiempo de trabajo en {} horas y {} minutos".format(horas,minutos))