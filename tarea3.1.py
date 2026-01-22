import math, os
os.system("cls")

print("1-Triangulo")
print("2-Cuadrado")
print("3-Circulo")
print("4-Pentagono")
print("5-Salir")
op=int(input("Seleccione una Opcion:"))

if op==1:
    print("Area de Triangulo")
    altura=int(input("Ingrese la Altura:"))
    base=int(input("Ingrese la Base:"))
    area=(base*altura)/2
    print("El Area del Triangulo es:",area)
else:
    if op==2:
        print("Area de Cuadrado")
        lado=int(input("Ingrese la Medida de un Lado:"))
        area=lado*lado
        print("El Area del Cuadrado es:",area)
    else:
        if op==3:
            print("Area de Circulo")
            radio=int(input("Ingrese el Radio:"))
            area=3.1416*(radio**2)
            print("El Area del Circulo es:",area)
        else:
            if op==4:
                print("Area de Pentagono")
                perimetro=int(input("Ingrese el Perimetro:"))
                apotema=int(input("Ingrese el Apotema:"))
                area=(perimetro*apotema)/2
                print("El Area del Pentagono es:",area)
            else:
                if op==5:
                    print("Hasta la Proxima")