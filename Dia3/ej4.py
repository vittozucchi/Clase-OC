def numeromasgrande(n1,n2,n3):
    if n1>n2 & n1>n3:
        return n1
    elif n2>n1 & n2>n3:
        return n2
    else:
        return n3

lista=[]        
for j in range(3):
    i=int(input("Ingrese un numero: "))
    lista.append(i)
print(numeromasgrande(lista[0],lista[1],lista[2]))


        

