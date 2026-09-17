def celsius_a_farenheit(cel):
    calc= (cel * 9/5)+32
    return calc
num=float(input("Pone grados celsius: "))
print(celsius_a_farenheit(num))
