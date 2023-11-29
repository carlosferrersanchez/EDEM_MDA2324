# RETO 9

# Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no

def es_bisiesto(ano:int) -> bool:
    if ano%4 == 0 and (ano%100 != 0 or ano%400 == 0):
        return(True)
    else:
        return(False)
    
ano = int(input("Escribe un año para saber si es bisiesto o no: "))

if(es_bisiesto(ano) == True):
    print("Es un año bisiesto! :)\n")
else:
    print("NO es un año bisiesto! :(\n")