while True:
    nombre = str(input("Ingresa tu nombre: ")).strip()
    if nombre:
        break
    print("Campo Vacío. Intente Otra Vez.")

while True:
    apellido = str(input("Ingresa tu apellido: ")).strip()
    if apellido:
        break
    print("Campo Vacío. Intente Otra Vez.")

nombre_completo = nombre + " " + apellido

print("Tu nombre completo es:", nombre_completo)