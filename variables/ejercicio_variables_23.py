# Ejercicio 23: Estimar el gasto típico de comida de un estudiante

# Pedimos al usuario cuántas veces a la semana come en la cafetería
veces_cafeteria = int(input("¿Cuántas veces a la semana comes en la cafetería? "))

# Pedimos el precio de un almuerzo típico en la cafetería
precio_almuerzo = float(input("¿Cuál es el precio de un almuerzo típico? "))

# Pedimos el dinero gastado en la compra de alimentos durante la semana
gastos_compra = float(input("¿Cuánto dinero gastas en la compra de alimentos durante la semana? "))

# Calculamos el gasto semanal total
gasto_semanal = (veces_cafeteria * precio_almuerzo) + gastos_compra

# Calculamos el gasto diario promedio
gasto_diario = gasto_semanal / 7

# Mostramos los resultados
print("Gasto promedio en comida:")
print(f"Diario: {gasto_diario} euros")
print(f"Semanal: {gasto_semanal} euros")
