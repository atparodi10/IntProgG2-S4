# Pide nombre y apellido y muestra un posible correo:
# nombre.apellido@miuniversidad.edu.ni

nombre = input("Ingrese su nombre: ").strip().lower()
apellido = input("Ingrese su apellido: ").strip().lower()


nombre = nombre.replace(" ", "")
apellido = apellido.replace(" ", "")

correo = f"{nombre}.{apellido}@uamv.edu.ni"

print("Correo generado:", correo)