# Solicita el nombre, precio de un producto y un porcentaje de descuento. Muestra el
# nombre del producto y precio final luego de aplicar el descuento.
while True:
    nombre = str(input("Ingresa el nombre del producto: ")).strip()
    if nombre:
        break
    print("Campo Vacío, Complete el espacio.")

precio = float(input(f"Ingresa el precio de {nombre}: "))
while precio <= 0:
    print("Monto Invalido. Verifique el precio.")
    precio = float(input(f"Ingresa el precio de {nombre}: "))

descuento = float(input("Ingresa el porcentaje del descuento a aplicar: "))
while descuento <= 0: 
    print("Monto Invalido. Intente Otra Vez.")
    descuento = float(input("Ingresa el porcentaje del descuento a aplicar: "))

aplicar_descuento = descuento / 100
valor_descuento = (aplicar_descuento * precio)
total = precio - valor_descuento

print("-"*5, "FACTURA","-"*5)
print(f"Nombre del Producto: {nombre}")
print(f"Precio: {precio: .2f}$")
print(f"Descuento: {descuento: .2f}%")
print(f"Descuento Aplicado: {valor_descuento}$")
print(f"Total: {total: .2f}")
print("-"*20)
