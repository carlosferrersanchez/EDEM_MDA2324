# RETO_7

# Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario 
# y la otra un texto introducido. El programa debe poder mostrar por pantalla si las dos cadenas de 
# texto son iguales sin tener en cuenta mayúsculas y minúsculas. 


password = "EDEM2324"
pass_usu = input("Escribe la contraseña: ")

password = password.lower()
pass_usu = pass_usu.lower()

if(password == pass_usu):
    print("Las contraseñas son iguales")
else:
    print("No son iguales")

