def email(nombre,apellido):
    
    return f"{nombre}.{apellido}@gmail.com"
ap=input("ingrese apellido")
nom=input("ingrese nombre")
print(email(nom,ap))