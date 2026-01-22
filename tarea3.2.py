import math,os
os.system("cls")

sueldo=int(input("Ingrese su sueldo: "))
if sueldo<1000:
    print("Su Sueldo Neto es: ",sueldo)
else:
    if sueldo<=2000:
        impuesto=sueldo*0.10
        suelNeto=sueldo-impuesto
        print("Su Sueldo Neto es: ",suelNeto)
    else:
        if sueldo>2000:
            impuesto=sueldo*0.20
            suelNeto=sueldo-impuesto
            print("Su Sueldo Neto es: ",suelNeto)