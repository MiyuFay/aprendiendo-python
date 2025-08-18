# Ejercicio 11: Resolver una ecuación cuadrática de la forma ax² + bx + c

# Importamos la función sqrt del módulo math para calcular raíces cuadradas
from math import sqrt

# Pedimos al usuario los valores de a, b y c
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))

# Calculamos el discriminante
discriminante = b ** 2 - 4 * a * c

# Calculamos las dos raíces usando la fórmula cuadrática
raiz1 = (-b + sqrt(discriminante)) / (2 * a)
raiz2 = (-b - sqrt(discriminante)) / (2 * a)

# Mostramos los resultados con dos decimales
print(f"Las raíces son {raiz1:.2f} y {raiz2:.2f}")
