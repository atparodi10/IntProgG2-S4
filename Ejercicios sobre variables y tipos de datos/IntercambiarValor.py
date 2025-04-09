# Diseña un algoritmo que intercambie el valor de dos variables numéricas. Usa una
# variable auxiliar para hacerlo.

a = float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))

print(f"\nValores antes del intercambio:\nA = {a}, B = {b}")

aux = a
a = b
b = aux

print(f"\nValores después del intercambio:\nA = {a}, B = {b}")

