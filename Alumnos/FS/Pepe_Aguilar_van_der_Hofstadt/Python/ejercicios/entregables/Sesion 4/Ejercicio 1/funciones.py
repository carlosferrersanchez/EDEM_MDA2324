
def lista_primos(min:int, max:int):     # devuelve los valores primos
    if min > max:
        c = min
        min = max
        max = c

    for num in range(min, max+1):
        primo = True
        for div in range(2,num):
            if num%div == 0:
                primo = False
                break
        if primo == True:
            print(f"- {num}")


def es_primo(num:int) -> bool:          # devuelve si un numero es primo o no
    if num == 1: return True
    for divisible in range(2,num):
        if num%divisible == 0:
            return False
    return True

def es_bisiesto(ano:int) -> bool:       # devuelve si un año es bisisto o no
    if ano%4 == 0 and (ano%100 != 0 or ano%400 == 0):
        return(True)
    else:
        return(False)
    
exit = False
while(exit == False):
    print(f"Probador de funciones")
    opt = input("[1]. Probar las funciones \n[X]. No probar las funciones\n")
    
    if(opt == '1'):
        print("Lista primos.")
        min = int(input("Escribe el valor minimo del rango: "))
        max = int(input("Escribe el valor maximo del rango: "))
        lista_primos(min, max)

        print("\nNumero primo.")
        num = int(input("Escribe un numero para saber si es primo: "))
        print(es_primo(num))

        print("\nAño bisiesto.")
        num = int(input("Escribe un año para saber si es bisiesto: "))
        print(es_bisiesto(num))
        print("\n")
    elif(opt == 'X'):
        exit = True