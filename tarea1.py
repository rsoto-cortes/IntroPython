import math, os

os.system("cls")

edad1=int(input("Ingrese la primer edad: "))
edad2=int(input("Ingrese la segunda edad: "))

if edad1>edad2:
    print("La primer persona es mayor")
else:
    if edad1<edad2:
        print("La segunda persona es mayor")
if edad1==edad2:
    print("Las dos personas tienen la misma edad")