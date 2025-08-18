# Ejercicio 5: Mostrar magnitud de un número según su valor

try:
    # Pedimos al usuario un número entero
    numero = int(input("Escribe un número entero: "))

    # Comprobamos las diferentes magnitudes
    if numero < 2000:
        print("Este número es menor que 2000")
    if numero < 500:
        print("Este número es menor que 500")
    if numero < 50:
        print("Este número es menor que 50")

    # Mensaje final
    print("¡Gracias por participar!")

except ValueError:
    print("Entrada inválida. Por favor, escribe un número entero.")
