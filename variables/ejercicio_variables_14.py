# Ejercicio 14: Mostrar información de un candidato para un trabajo

# Datos del candidato
nombre = "Ana Sanchez"
edad = 28
habilidad1 = "Python"
nivel1 = "principiante"
habilidad2 = "Java"
nivel2 = "avanzado"
habilidad3 = "Diseño Web"
nivel3 = "intermedio"
salario_min = 1800
salario_max = 2500

# Mostramos la información correctamente formateada
print(f'Mi nombre es {nombre}, tengo {edad} años')
print()
print('Mis habilidades son')
print(f' - {habilidad1} ({nivel1})')
print(f' - {habilidad2} ({nivel2})')
print(f' - {habilidad3} ({nivel3})')
print()
print(f'Busco un trabajo con un salario de {salario_min}-{salario_max} euros al mes')