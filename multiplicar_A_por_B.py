
A=int(input("Ingrese el primer numero:"))
B=int(input("Ingrese el segundo numero:"))
cont=0
res=0
while cont<B:
    res=res+A
    cont=cont+1
print("{} por {} es igual a {}".format(A,B,res))