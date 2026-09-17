frase=str(input("ingrese una frase "))
cont=0


for prom in frase:
    if prom in "aAeEiIoOuU":
        cont=cont+1

print(cont)