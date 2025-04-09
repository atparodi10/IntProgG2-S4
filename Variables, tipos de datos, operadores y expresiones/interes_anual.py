# Una persona recibe un préstamo de 10,000.00 de un banco y desea saber cuánto 
# pagará de interés, si el banco le cobra una tasa del 27% anual.

# i = capital * interes * años

tiempo = int(input("Ingrese el tiempo establecido según el contrato del préstamo: "))
while tiempo <= 0:
    print("Ingresa un tiempo valido. Intenta Otra Vez.")
    tiempo = int(input("Ingrese el tiempo establecido según el contrato del préstamo: "))
    
interes_anual = 10000 * 0.27
interes_total = 10000 * 0.27 * tiempo
deuda_total = 10000 + interes_total

print(f"El interes anual es de: {interes_anual: .2f}")
print(f"Según el tiempo definido la dueda total será de: {deuda_total: .2f}")