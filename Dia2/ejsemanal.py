import random
compu= random.randint(1,100)

user=int(input("Adivine el numero: "))

if compu==user:
    print("Ganaste")


while user !=compu:


    if user>compu:
        print("el numero es mas pequeño")
    else:
        print("el numero es mas grande")
    
