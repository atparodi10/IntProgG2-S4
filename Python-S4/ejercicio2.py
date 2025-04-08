cantidad = 10
precio = 200
total = cantidad * precio
def ftexto(texto):
    return f"{texto:<10}"
print(f"{ftexto('Cantidad: ')} {cantidad:>6}")
print(f"{ftexto('Precio: ')} {precio:>6}")
print(f"{ftexto('Total: ')} {total:>6}")