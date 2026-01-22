import math, os

os.system("cls")

print("1-Suma")
print("2-Resta")
print("3-Multiplicacion")
print("4-Divicion")

op=int(input("Elija una Opcion: "))

num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

if op==1:
    suma=num1+num2
    print("El resultado de la suma es:",suma)
else:
    if op==2:
        resta=num1-num2
        print("El resultado de la resta es:",resta)
    else:
        if op==3:
            multi=num1*num2
            print("El resultado de la multiplicacion es:",multi)
        else:
            if op==4:
                div=num1/num2
                print("El resultado de la division es:",div)
            else:print("Fin del programa")    
