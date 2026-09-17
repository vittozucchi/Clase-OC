def calc_prec_fin(precio,descuento):
    calc= (descuento*precio)/100
    calc1= precio-descuento
    return calc1
prec=float(input("Ingrese el precio "))
desc=int(input("Ingrese el descuento: "))
print(calc_prec_fin(prec,desc))