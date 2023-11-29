listaAnos = range(1200)

for ano in listaAnos:
    if ano%4 == 0 and (ano%100 != 0 or ano%400 == 0):
        print(f"{ano} - es bisiesto")
    else:
        print(f"{ano}")