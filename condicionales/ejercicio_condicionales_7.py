# Ejercicio 7: Conversión de grados Fahrenheit a Celsius con aviso de frío

# Pedimos al usuario la temperatura en Fahrenheit
temperatura_f = float(input("Introduce una temperatura en grados Fahrenheit: "))

# Convertimos la temperatura a Celsius
temperatura_c = (temperatura_f - 32) * 5 / 9

# Mostramos la temperatura convertida
print(f"{temperatura_f} grados Fahrenheit equivalen a {temperatura_c} grados Celsius")

# Avisamos si hace mucho frío
if temperatura_c < 0:
    print("¡Brr! ¡Hace mucho frío aquí!")
