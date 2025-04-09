# Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra
# los tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrer
# la ruta en una semana cualquiera.


lunes = float(input("Tiempo del lunes (minutos): "))
miercoles = float(input("Tiempo del miércoles (minutos): "))
viernes = float(input("Tiempo del viernes (minutos): "))

promedio = (lunes + miercoles + viernes) / 3

print(f"El tiempo promedio para recorrer la ruta es: {promedio} minutos")