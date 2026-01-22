#hacer un programa que permita pedir al usuario ingresar 5 calificaciones
#y despues de pedirlas imprimir el promedio

import math, os
os.system("cls")
suma=0
i=1
while i<=5:
    i+=1
    calif=(int(input("Ingrese su Calificacion: ")))
    suma=suma+calif
prom=suma/5
print("Su Promedio es de: ",prom)