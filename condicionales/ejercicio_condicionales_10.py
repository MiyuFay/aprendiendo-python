# Ejercicio 10: Sugerencia de ropa según la previsión del tiempo

# Pedimos al usuario la temperatura y si lloverá
temperatura = float(input("Temperatura para mañana (°C): "))
lluvia = input("¿Lloverá mañana? (sí/no): ").lower().strip()

# Sugerencias de ropa según la temperatura
if temperatura > 20:
    print("Lleva vaqueros y una camiseta")
elif 20 >= temperatura > 10:
    print("""Lleva vaqueros y una camiseta
Te recomiendo un suéter también""")
elif 10 >= temperatura > 5:
    print("""Lleva vaqueros y una camiseta
Te recomiendo un suéter también
Lleva una chaqueta""")
elif temperatura <= 5:
    print("""Lleva vaqueros y una camiseta
Te recomiendo un suéter también
Lleva una chaqueta
Mejor un abrigo calentito
Piensa en guantes""")

# Comprobamos si va a llover
if lluvia == 'sí':
    print("¡No olvides tu paraguas!")
