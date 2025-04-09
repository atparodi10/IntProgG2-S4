# Calcular salario segun horas trabajadas, descontar la renta de 5% e imprimir datos

# Entrada de datos
nombre = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
precio_por_hora = float(input("Ingrese el precio que cobra por hora: "))

# Cálculos
sueldo_bruto = horas_trabajadas * precio_por_hora
descuento_renta = sueldo_bruto * 0.05
salario_neto = sueldo_bruto - descuento_renta

# Salida
print("\n--- Detalle del Pago ---")
print(f"Nombre del trabajador: {nombre}")
print(f"Sueldo bruto: ${sueldo_bruto:.2f}")
print(f"Descuento por renta (5%): ${descuento_renta:.2f}")
print(f"Salario neto a pagar: ${salario_neto:.2f}")
