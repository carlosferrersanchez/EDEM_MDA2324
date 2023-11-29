# RETO_6

# Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("Que edad tienes? "))

if(edad >= 18):
    print("Eres mayor de edad.")
else:
    faltan = 18 - edad
    print(f"Eres menor, te quedan {faltan} año/s para ser mayor de edad")
