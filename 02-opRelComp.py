import math, os

os.system("cls")

print("|----- Grupo ICO201-9, ICO 201-14-----|")

num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))

suma=num1+num2
print("La suma de {} con {} es: {}".format(num1,num2,suma))

resta=num1-num2
print("La resta de {} con {} es: {}".format(num1,num2,resta))

multiplicacion=num1*num2
print("La multiplicacion de {} por {} es: {}".format(num1,num2,multiplicacion))

divison=num1/num2
print("La division de {} entre {} es: {}".format(num1,num2,divison))

potencia=num1**num2
print("La potencia de {} y {} es: {}".format(num1,num2,potencia))

print("Operaciones Basicas: \n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n")

opcion=input("Ingrese la operacion a realizar (1/2/3/4): ")



val1=3
val2=5

temp=val1>val2 #False
temp=val1==val2 #False
temp=val1<val2 #True
temp=val1>=val2 #False
temp=val1<=val2  #True
temp=val1!=val2 #True


print("El valor de la comparacion es: ", temp)

tem2= not(val1>val2) and (val1<val2) #true

print("El valor de la comparacion con NOT y AND es: ", tem2)

