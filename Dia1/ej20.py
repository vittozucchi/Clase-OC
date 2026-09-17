programa="piedra"
user=str(input("ingrese lo que quiera jugar "))

if programa==user:
    print("empate")

if user=="papel":
    print("ganaste")

if user=="tijera":
    print("perdiste")

else:
    print("ingrese piedra, papel o tijera")