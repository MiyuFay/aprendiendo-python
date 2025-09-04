# Ejercicio 14: Separar parte entera y decimal de un número

# El programa pide al usuario que escriba un número decimal positivo.
# Muestra por pantalla:
#   - La parte entera del número
#   - La parte decimal (restando la parte entera al número original)

# Pedimos el número al usuario
numero = float(input("Escribe un número decimal positivo: "))

# Obtenemos la parte entera usando int()
entero = int(numero)

# Calculamos la parte decimal restando el entero al número original
decimal = numero - entero

# Mostramos los resultados
print(f"Parte entera: {entero}")
print(f"Parte decimal: {decimal}")
