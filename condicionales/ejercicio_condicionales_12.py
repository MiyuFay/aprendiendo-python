# Ejercicio 12: Comprobar si un número es mayor que 100 y restarle 100

# El programa pide al usuario un número entero.
# Si el número es mayor que 100:
#   - Informa de que el número es mayor a 100
#   - Le resta 100
#   - Muestra el nuevo valor
# Finalmente, imprime el número como "número de la suerte".

# Pedimos un número al usuario
numero = int(input("Introduce un número: "))

# Verificamos si es mayor que 100
if numero > 100:
    print("El número es mayor que 100")
    numero = numero - 100
    print("Ahora su valor ha disminuido en 100")
    print("Su valor actual es " + str(numero))

# Mensaje final
print(str(numero) + " es mi número de la suerte")
print("¡Que tengas un buen día!")
