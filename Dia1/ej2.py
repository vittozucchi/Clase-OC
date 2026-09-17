while True:
    try:
        cuenta=float(input("cuanto es? "))

        porcentaje= int(input("Cuanto porcentaje quiere dejar? "))

        calculo=(cuenta*porcentaje)/100
        print(calculo)

        print(cuenta+calculo)
        break
    except ValueError:
        print("ingrese la cuenta en numeros")

