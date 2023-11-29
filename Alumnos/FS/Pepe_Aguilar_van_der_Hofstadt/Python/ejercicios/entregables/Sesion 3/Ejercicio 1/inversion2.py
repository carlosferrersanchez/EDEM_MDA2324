# Lo hago un poco más completo al enunciado ya que lo hice así en clase

def inversion() -> float:

    dinero = float(input("Cuanto dinero tienes para invertir (€)? "))
    interes = float(input("Que interés quieres? \nEscribelo en decimal, ej 5% = 0.05. "))
    ano = int(input("Cuantos años quieres la inversión? "))
    profit = dinero*interes*ano
    '''tipo = str(type(dinero)).split("'")[1]      # averiguar que tipo de dato es
    print(f"El tipo del dato es {tipo}")'''
    print(f"En {ano} años tendrás {profit}€ de profit")
    return(profit)

# Numero primo

def es_primo(num:int) -> bool:
    if num == 1: return True
    for divisible in range(2,num):
        if num%divisible == 0:
            return False
    return True
#print(es_primo(70))

# Año bisiesto 

def es_bisiesto(ano:int) -> bool:
    if ano%4 == 0 and (ano%100 != 0 or ano%400 == 0):
        return(True)
    else:
        return(False)


exit = False
while(exit == False):
    print(f"Bienvenido al menú principal de PEP S.L. Qué desea hacer?")
    option = input("1. Cálculo de inversión.\n2. Calcula si es primo.\n3. Calcula si es año bisiesto\nX. Press 'x' to exit\n")

    if(option == '1'):
        inversion()
        print("\n")

    elif(option == '2'):
        primo = int(input("Escribe un número para saber si es primo o no: "))
        if(es_primo(primo) == True):
            print("Es número primo! :)\n")
        else:
            print("NO es número primo! :(\n")

    elif(option == '3'):
        ano = int(input("Escribe un año para saber si es bisiesto o no: "))
        if(es_bisiesto(ano) == True):
            print("Es un año bisiesto! :)\n")
        else:
            print("NO es un año bisiesto! :(\n")

    elif(option == 'x' or option == 'X'):
        print("See you soon!!!")
        exit = True
    