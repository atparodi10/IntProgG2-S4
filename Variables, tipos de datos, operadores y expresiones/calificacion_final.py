# Calcula la calificación final de un estudiante con ponderaciones:
# Tareas: 30%
# Examen parcial: 30%
# Examen final: 40%

tarea = float(input("Ingresa la nota total de tareas (0-100): "))
while tarea < 0 or tarea > 100:
    print("Nota Invalida. Intente Otra Vez.")
    tarea = float(input("Ingresa la nota total de tareas (0-100): "))

examen_parcial = float(input("Ingresa la nota del examen parcial(0-100): "))
while examen_parcial < 0 or examen_parcial > 100:
    print("Nota Invalida. Intente Otra Vez.")
    examen_parcial = float(input("Ingresa la nota del examen parcial(0-100): "))

examen_final = float(input("Ingresa la nota del examen final(0-100): "))
while examen_parcial < 0 or examen_final > 100:
    print("Nota Invalida. Intente Otra Vez.")
    examen_final = float(input("Ingresa la nota del examen final(0-100): "))

nota_tareas = tarea * 0.30
nota_examen_parcial = examen_parcial * 0.30
nota_examen_final = examen_final * 0.40

nota_final = nota_tareas + nota_examen_parcial + nota_examen_final

print(f"Nota de Tareas: {nota_tareas: .2f}")
print(f"Nota de Examen Parcial: {nota_examen_parcial: .2f}")
print(f"Nota Examen Final: {examen_final: .2f}")
print(f"Nota Final: {nota_final: .2f}")