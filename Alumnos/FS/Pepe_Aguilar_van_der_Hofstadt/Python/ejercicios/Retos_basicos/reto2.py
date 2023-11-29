# RETO 2
# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

def calculoImpares(final:int, inicio:int = 1) -> list:          
    listaimpares = []
    if inicio > final:
        c = inicio
        inicio = final
        final = c
    for n in range(inicio,final+1):
        if n%2 != 0:
            listaimpares.append(n)
    return listaimpares

# no se chequea que el ususario meta un numero
print("Welcome to the odds numbers in a range program")
num1 = int(input("Please enter a number of the lowest number in your range: "))
num2 = int(input("Now the higest: "))

print(calculoImpares(num2,num1))
