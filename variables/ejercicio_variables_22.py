# Ejercicio 22: Pedir cuatro números al usuario
# y mostrar la suma y la media de esos números

# Pedimos al usuario los cuatro números (convertidos a entero)
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))
numero3 = int(input("Escribe el tercer número: "))
numero4 = int(input("Escribe el cuarto número: "))

# Calculamos la suma de los números
suma = numero1 + numero2 + numero3 + numero4

# Calculamos la media
media = suma / 4

# Mostramos los resultados en pantalla
print(f"La suma de los números es {suma} y la media es {media}")
