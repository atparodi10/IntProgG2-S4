# Adivinar un número
import random

while True:
    numero_secreto = random.randint(1, 10)

    numero_usuario = int(input("Ingrese un numero entre 1 y 10: "))

    if numero_usuario == numero_secreto:
        print("Adivinaste el número.")
        print(f"{numero_secreto} - {numero_usuario}")
        break

    else: 
        print("No adivinaste el número. intenta Otra Vez.")
    
    if numero_usuario > numero_secreto:
        print("El numero es menor.")
        
    else:
        print("El numero es Mayor.")