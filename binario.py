#hacer un programa que le pida al usuario un numero entre 1 y 100 y que me de el numero en binario#
import math, os
os.system("cls")

num=int(input("Ingrese un numero entre 1 y 100: "))

while num<1 or num>100:
    print("Numero fuera de rango")
    num=int(input("Intenta de nuevo. Ingrese un numero entre 1 y 100: "))

print("Numero Valido:", num)

binario= ""
while num>0:
    binario=str(num%2)+binario
    num=num//2
print("El numero binario es:",binario)    


""" OTRA FORMA DE HACERLO
while True: 
    num=int(input("Ingrese un numero entre 1 y 100: "))
    if 1<= num <=100:
        break
    print("Numero fuera de rango")"""
