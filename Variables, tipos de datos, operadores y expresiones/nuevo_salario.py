# Calcular el nuevo salario de un empleado si obtuvo un incremento del 8% sobre su
# salario actual y un descuento de 2,5% por servicios.

salario = float(input("Ingresa el salario neto: "))
while salario <= 0:
    print("Cantidad no valida. Intente Otra Vez.")
    salario = float(input("Ingresa el salario neto: "))
    
incremento = salario * 0.08
salario_incremento = salario + incremento
descuento = salario_incremento * 0.025
salario_total = salario_incremento - descuento

print(f"Salario: {salario: .2f}")
print(f"Incremento 8%: {incremento: .2f}")
print(f"Salario con el Incremento: {salario_incremento: .2f}")
print(f"Descuento 2,5%: {descuento: .2f}")
print(f"Salario Total: {salario_total: .2f}")
