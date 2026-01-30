

num=int(input("Ingrese un numero : "))
x=range(10)
s=1


print("Tabla de multiplicar del numero: ",num)
for i in x :
    mult=num*s
    print("{} x {} = {}".format(num,s,mult))
    s=s+1 
    
    