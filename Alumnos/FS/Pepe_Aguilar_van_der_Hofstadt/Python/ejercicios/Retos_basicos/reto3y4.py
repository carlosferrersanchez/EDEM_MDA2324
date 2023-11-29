# RETO 3 Y 4

def invert_list(lista:list) -> []:
    return reversed(lista)

# RETO 3
# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso**.**

print("RETO 3. 1 al 100 orden inverso")
invers = list(range(1,101))
print(*invert_list(invers))

# RETO 4
# Escribe un programa que sea capaz de mostrar los elementos de una lista en orden inverso al original.

print("\nRETO 4. a partir de una lista, invierte el orden")
inv_lista = []
check = False
while check == False:
    element = input("Write numbers for the list, to exit press 'exit': ")
    if element == "exit":
        check = True
    else:
        inv_lista.append(element)

print(*invert_list(inv_lista))

