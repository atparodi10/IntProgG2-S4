# Solicita el precio de 3 productos y muestra:
# Subtotal
# IVA (15%)
# Total a pagar
while True:
    prodcuto1 = str(input("Ingresa el nombre del primer producto: ")).strip()
    if prodcuto1:
        break
    print("Campo Vacío. Intente Otra Vez.")

while True:
    prodcuto2 = str(input("Ingresa el nombre del segundo producto: ")).strip()
    if prodcuto2:
        break
    print("Campo Vacío. Intente Otra Vez.")


while True:
    prodcuto3 = str(input("Ingresa el nombre del primer producto: ")).strip()
    if prodcuto3:
        break
    print("Campo Vacío. Intente Otra Vez.")

precio1 = float(input(f"Ingresa el precio de {prodcuto1}: "))
while precio1 <= 0:
    print("Monto Invalido. Intente Otra Vez.")
    precio1 = float(input(f"Ingresa el precio de {prodcuto1}: "))
    
precio2 = float(input(f"Ingresa el precio de {prodcuto2}: "))
while precio1 <= 0:
    print("Monto Invalido. Intente Otra Vez.")
    precio2 = float(input(f"Ingresa el precio de {prodcuto2}: "))

precio3 = float(input(f"Ingresa el precio de {prodcuto3}: "))
while precio1 <= 0:
    print("Monto Invalido. Intente Otra Vez.")
    precio3 = float(input(f"Ingresa el precio de {prodcuto3}: "))

subtotal = precio1 + precio2 + precio3
iva = subtotal * 0.15
total = subtotal + iva

print("-"*5, "FACTURA","-"*5)
print(f"{prodcuto1}\t{prodcuto2}\t{prodcuto3}")
print(f"\t{precio1: .2f}$ \t{precio2: .2f} \t\t\t{precio3: .2f}")
print(f"Subtotal: {subtotal: .2f}$")
print(f"IVA(15%): {iva: .2f}")
print(f"Total: {total: .2f}")
print("-"*20)