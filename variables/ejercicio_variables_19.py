# Ejercicio 19: Pedir al usuario un número de días
# y calcular el número de segundos que hay en esos días

# Pedimos al usuario la cantidad de días
dias = int(input("¿Cuántos días? "))

# Calculamos los segundos multiplicando los días por 86400 (segundos por día)
segundos = dias * 86400

# Mostramos el resultado
print(f"Segundos en esos días: {segundos}")
