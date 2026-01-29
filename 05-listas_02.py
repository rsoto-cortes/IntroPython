"""
pedir 5 sueldos agregar a lista e imprimir
"""

sueldos=[]
pr=0
cont=0
valM=0
valm=0

while cont<=4:
    tem=float(input("Dame el sueldo "+str({cont+1})))
    sueldos.append(tem)
    pr=pr+tem
    
    if cont==0:
        valM=tem
        Valm=tem
    else:
        if tem>valM:
            valM=tem
        if tem<valm:
            valm=tem
        
    cont+=1
        
    
print("Los sueldos son: ",sueldos)
print("El promedio de los sueldos es: ",pr/5)
print("El sueldo mayor es: ",valM)
print("El sueldo menor es:",valm)