numsecret= 8

user=int(input("Ingrese el numero entre 1 y 10: "))

if user<1 or user>10:
    print("Ingrese un numero valido")

else:
    if user==numsecret:
        print("Ganaste")
    
    else:
        print("Intente de nuevo")