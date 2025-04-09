# Calcular la edad en 10 años

anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
anio_actual = int(input("Ingrese el año actual: "))

edad_actual = anio_actual - anio_nacimiento
edad_en_10_anios = edad_actual + 10

# Salida
print(f"\nEdad actual: {edad_actual} años")
print(f"Edad dentro de 10 años: {edad_en_10_anios} años")
