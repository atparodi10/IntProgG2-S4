# Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos
edad = int(input("Ingrese su edad: "))

pulsaciones = (220 - edad) / 10

print(f"Número de pulsaciones en 10 segundos: {pulsaciones}")