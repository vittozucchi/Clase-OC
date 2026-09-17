def minutosahoras(minu):
    hora= int(minu%60)
    calc=minu-hora
    calc1= int(calc/60)

    print(f"Son las {calc1} horas con {hora} minutos")
area=int(input())
(minutosahoras(area))



