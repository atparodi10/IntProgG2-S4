# Obtener la cantidad de dinero que recibirá cada área para cualquier monto presupuestal.

presupuesto = float(input("Ingrese el presupuesto total del hospital: "))

urgencias = presupuesto  * 0.37
pediatria = presupuesto * 0.42
traumatologia = presupuesto * 0.21

print("Distribución del presupuesto:")
print(f"Urgencias: {urgencias}")
print(f"Pediatría: {pediatria}")
print(f"Traumatología: {traumatologia}")