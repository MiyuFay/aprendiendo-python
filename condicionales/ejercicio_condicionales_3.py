# Ejercicio 3: Calcular el valor absoluto de un número

# Este ejercicio se ha adaptado de ejercicios disponibles en la web:
# https://programming-23.mooc.fi/part-1/5-conditional-statements

# Pedimos al usuario que escriba un número entero
numero = int(input("Escribe un número: "))

# Si el número es negativo, mostramos su valor absoluto multiplicando por -1
if numero < 0:
    print(f"El valor absoluto de este número es {numero * -1}")
else:
    # Si no es negativo, lo mostramos tal cual
    print(f"El valor absoluto de este número es {numero}")

