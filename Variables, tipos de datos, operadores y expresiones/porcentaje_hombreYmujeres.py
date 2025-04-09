# Calcular el porcentaje de mujeres y de hombres
try:
    hombre = int(input("Ingrese la cantidad de Varones en el salón: "))
    while hombre < 0:
        print("Ingresa una cantidad valida.")
        hombre = int(input("Ingrese la cantidad de Varones en el salón: "))
    
    mujeres =  int(input("Ingrese la cantidad de Mujeres en el salón: "))
    while mujeres < 0:
        print("Ingresa una cantidad valida.")
        mujeres = int(input("Ingrese la cantidad de Mujeres en el salón: "))

    total_estudiantes = hombre + mujeres
    if total_estudiantes == 0:
        print("No puede haber 0 estudiantes en un salon.")
        
    else:
        porcentaje_hombre = (hombre / total_estudiantes) * 100
        porcentaje_mujeres = (mujeres / total_estudiantes) * 100

        print(f"Total de Estudiantes: {total_estudiantes}")
        print(f"Total de Hombres: {hombre}")
        print(f"Total de Mujeres: {mujeres}")
        print(f"Hombres: {porcentaje_hombre: .2f}%")
        print(f"Mujeres: {porcentaje_mujeres: .2f}%")
    
except ValueError:
    print("Ingresa Valores enteros validos.")
    
