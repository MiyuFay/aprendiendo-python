# Ejercicio 9: Calcular la bonificación de fin de año en una tarjeta de fidelidad

# Pedimos al usuario la cantidad de puntos en su tarjeta
puntos = int(input("¿Cuántos puntos tienes en tu tarjeta? "))

# Calculamos la bonificación según los puntos
if puntos < 100:
    puntos *= 1.1  # Bonificación del 10 %
    print("Tu bonificación es del 10 %")
else:
    puntos *= 1.15  # Bonificación del 15 %
    print("Tu bonificación es del 15 %")

# Mostramos la cantidad final de puntos
print(f"Ahora tienes {puntos} puntos")
