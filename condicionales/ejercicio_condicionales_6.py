# Ejercicio 6: Calculadora básica con condicionales

# Pedimos al usuario dos números
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))

# Pedimos la operación a realizar
operacion = input("Escribe la operación (sumar, restar, multiplicar): ")

# Realizamos la operación según el valor ingresado
if operacion == "sumar":
    print(f"{numero1} + {numero2} = {numero1 + numero2}")
elif operacion == "restar":
    print(f"{numero1} - {numero2} = {numero1 - numero2}")
elif operacion == "multiplicar":
    print(f"{numero1} * {numero2} = {numero1 * numero2}")
# Si el usuario ingresa cualquier otra cosa, no se muestra nada
