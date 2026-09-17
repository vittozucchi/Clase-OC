while True:
    try:
        ano= int(input("Cuando naciste? ")) 
        calculo= 2026 - ano
        if calculo>=18:
            print("Eres mayor de edad, pasas")
    

        if calculo<18:
            print("Eres menor de edad, no pasas")
        

    except ValueError:
        print("ingrese su edad en numeros")
    
    
    