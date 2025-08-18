# Ejercicio condicionales 4: Pedir el nombre y calcular el precio de las raciones

# Pedimos el nombre del usuario
nombre = input("¿Cuál es tu nombre?: ")
precio_racion = 6.50  # Precio de una ración

# Si el usuario NO se llama Carlos, preguntamos cuántas raciones quiere
if nombre != "Carlos":
    cantidad = int(input("¿Cuántas raciones deseas?: "))
    total = precio_racion * cantidad
    print(f"El precio total es {total} euros")
    print("¡Siguiente por favor!")
else:
    print("¡Siguiente por favor!")
