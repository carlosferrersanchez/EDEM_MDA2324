# RETO_1

# crea variables que representen los siguientes datos de un contacto e imprimelas

name = input("Escribe tu nombre: ")

print(f"Hello {name} welcome to this program \nI'm gonna need some information about you.")

surname = input("Surname: ")
age = input("Age: ")                # se podria chequear que la edad esta correcta pero mucho texto para programa basico
mail = input("Email: ")
phone = input("Phone: ")

check = False
while(check == False):
    married = input("Married (y/n): ")
    if married == "y":
        check = True
        married = True
    elif married == "n":
        check = True
        married = False

check = False
while(check == False):
    sons = input("sons (y/n): ")
    if sons == "y":
        check = True
        sons = True
    elif sons == "n":
        check = True
        sons = False        

friends = []
check = False
while(check == False):
    any_friend = input("do you have more friends (y/n)?")
    if any_friend == "n":
        check = True        
    else:
        friendx = input("Write his/her name: ")
        friends.append(friendx)

films = []
check = False
while(check == False):
    any_film = input("Have you seen more films (y/n)?")
    if any_film == "n":
        check = True        
    else:
        filmx = input("Write its name: ")
        films.append(filmx)

print("\nCheck if it is correct.\n")
print(f"Name: {name}")
print(f"Surname: {surname}")
print(f"Age: {age}")
print(f"Email: {mail}")
print(f"Phone: {phone}")
print(f"Married: {married}")
print(f"Sons: {sons}")
print(f"Friends: {friends}")
print(f"Films: {films}")