nota=float(input("ingrese nota "))
    
if nota<0 or nota>10:
    print("Ingrese una nota existente")

elif nota>=6:
    print("aprobaste ")

else:
    print("desaprobado")