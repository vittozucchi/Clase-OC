
def retirar(dinero):
    saldo=1000
    if dinero>saldo:
        print("saldos insuficientes")
    elif saldo>dinero:
        print("La transaccion se ha hecho con exito")
        saldo=saldo-dinero
        print("Su saldo final es: ", saldo)

dineroo=int(input("ingrese el dinero a retirar: "))
while True:  
    try:
        pinn=int(input("Pin: "))
        def verifpin(pin):
            if pin==1234:
                return True
            else:
                return False
        if verifpin(pinn)==True:
            retirar(dineroo)

    except ValueError:
        print("Simbolos numericos")
        break
    



    
                       




    