import math, os
os.system("cls")

calif=int(input("Ingrese su Calificacion: "))
if calif>=7:
    if calif>=9:
        print("Excelente")
    else:
        print("Aprobado")
else:
    print(("Reprobado"))