# Ejercicio 13: Contar caracteres en una palabra

# El programa pide al usuario que escriba una palabra.
# Si la palabra tiene más de un carácter:
#   - Muestra el número de letras que contiene
# En cualquier caso:
#   - Finaliza con un mensaje de agradecimiento.

# Pedimos la palabra al usuario
palabra = input("Escribe una palabra: ")

# Calculamos la longitud de la palabra
longitud = len(palabra)

# Si la palabra tiene más de un carácter, mostramos su tamaño
if longitud > 1:
    print(f"La palabra '{palabra}' tiene {longitud} letras")

# Mensaje final
print("¡Gracias!")
