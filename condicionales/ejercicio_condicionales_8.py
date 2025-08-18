# Ejercicio 8: Calcular salario diario según horas trabajadas y día de la semana

# Pedimos al usuario el salario por hora, las horas trabajadas y el día de la semana
salario_hora = float(input("Introduce tu salario por hora: "))
horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))
dia_semana = input("Introduce el día de la semana: ").lower().strip()

# Calculamos el salario diario
if dia_semana == "domingo":
    salario_diario = (salario_hora * 2) * horas_trabajadas
else:
    salario_diario = salario_hora * horas_trabajadas

# Mostramos el resultado con un decimal
print(f"Salario diario: {salario_diario:.1f} euros")
