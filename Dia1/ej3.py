while True:
    try:
        numero=int(input("Ingrese un numero entero: "))

        calculo=numero%2

        if calculo==0:

            print("Es par")

        else:
            print("Es impar")
            break
    except ValueError:
        print("ingrese un numero entero porfavor")