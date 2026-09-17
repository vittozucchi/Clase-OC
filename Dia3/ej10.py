def puede_votar(edad):
    if edad>=18:
        return f"Sos mayor"
    else:
        return f"No puede votar"
    
user=int(input("Ingresa tu edad: "))
print(puede_votar(user))   