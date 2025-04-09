# Dado un total de cuenta y un porcentaje de propina (por ejemplo, 10%), calcula cuánto dejar de propina.

cuenta_total = float(input("Cuenta Total: "))
while cuenta_total <= 0:
    print("Monto Invalido. Intente Otra Vez.")
    cuenta_total = float(input("Cuenta Total: "))

print("Seleccione el porcentaje de propina: ")
propina = int(input("10% \n15% \n20% \n25% \n:"))

if propina == 10:
    porcentaje = 0.10

elif propina == 15:
    porcentaje = 0.15

elif propina == 20:
    porcentaje = 0.20

elif propina == 25:
    porcentaje = 0.25

else:
    print("Opción no valida. Se usará 10% por defecto.")
    porcentaje = 0.10

propina_total = cuenta_total * porcentaje

print(f"Total de Cuenta: {cuenta_total: .2f}")
print(f"Propina Seleccionada: {propina}%")
print(f"Propina Total: {propina_total: .2f}")