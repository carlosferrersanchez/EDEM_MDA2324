# RETO_5

# Pide la contraseña y mientras esta no ser correcta pidela de nuevo hasta 3 intentos

from random import seed
from random import randint

PASS = 'admin'

user_validation = False
intentos = 3

while(user_validation == False and intentos > 0):
    print(f'Intentos restantes {intentos}.')
    contra_usu = input('Por favor introduce la contraseña: ')

    if(contra_usu == PASS):
        print("Bienvenido al programa señor ADMIN :)\n")
        user_validation = True
    else:
        print('ERROR, CONTRASEÑA INCORRECTA')
        intentos -= 1

        if(intentos <= 0):
            print("Se te acabaron los intentos, ahora te entrará un troyano")
            for troy in range(4000):
                print(randint(1,1000000))
                print(randint(1,1000))
                print(randint(1,100000000000))
