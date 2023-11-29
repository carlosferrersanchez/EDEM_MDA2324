# RETO_8

# Escribe un programa que pueda decirte si un número (número entero) es primo o no

def es_primo(num:int) -> bool:
    if num == 1: return True
    for divisible in range(2,num):
        if num%divisible == 0:
            return False
    return True

num = int(input("Escribe un numero y te digo si es primo o no: "))

if(es_primo(num) == True):
    print("Es primo")
else:
    print("No es primo")