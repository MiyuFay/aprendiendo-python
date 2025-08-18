# Ejercicio 1: Calcular el número de grupos formados según el número de estudiantes y el tamaño deseado

# Este ejercicio se ha adaptado de ejercicios disponibles en la web:
# https://programming-23.mooc.fi/part-1/4-arithmetic-operations

# Pedimos al usuario el número total de estudiantes
total_estudiantes = int(input("Número total de estudiantes en el curso: "))

# Pedimos el tamaño deseado para cada grupo
tamano_grupo = int(input("Tamaño deseado de cada grupo: "))

# Calculamos el número de grupos enteros
numero_grupos = total_estudiantes // tamano_grupo

# Si sobran estudiantes que no caben en los grupos completos, se añade un grupo más
if total_estudiantes % tamano_grupo != 0:
    numero_grupos += 1

# Mostramos el resultado
print(f"Número de grupos formados: {numero_grupos}")

