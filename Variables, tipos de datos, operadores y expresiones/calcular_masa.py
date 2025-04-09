# Diseñe un algoritmo que lea los datos necesarios y calcule la masa
presion = float(input("Ingrese la presión: "))
volumen = float(input("Ingrese el volumen: "))
temperatura = float(input("Ingrese la temperatura en Fahrenheit: "))

masa = (presion * volumen) / (0.37 * (temperatura + 460))

print(f"La masa es: {masa}")