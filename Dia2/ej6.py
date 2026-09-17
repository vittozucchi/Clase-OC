agenda= {
    "pedro": 123,
    "juan": 456,
    "alan": 678,
}

user=str(input("Ingrese un nombre: "))

print(agenda.get(user, "No encontrado"))