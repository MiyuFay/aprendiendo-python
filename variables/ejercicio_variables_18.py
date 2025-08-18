# Ejercicio 18: Pedir al usuario su nombre y su año de nacimiento,
# y calcular la edad que tendrá al final del año 2025

# Pedimos al usuario su nombre
nombre = input("¿Cómo te llamas? ")

# Pedimos al usuario su año de nacimiento (convertimos a entero)
anio_nacimiento = int(input("¿En qué año naciste? "))

# Definimos el año para calcular la edad
anio_actual = 2025

# Calculamos la edad
edad = anio_actual - anio_nacimiento

# Mostramos el resultado
print(f"Hola {nombre}, tendrás {edad} años al final del año {anio_actual}.")
