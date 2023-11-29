# RETO_1_av

# VENTA DE DISCOS.
# Venta de los discos almacenados en stock (en vez de diccionarios utilizaré POO)
# En vez de crear los discos uno a uno, haré un programa que los cree aleatoriamente.

# El programa debe dar a elegir al usuario que discos comprar y imprimir un ticket de compra
# Los discos de Black Metal y de Electro tienen 30% de descuento

import requests
import random
from datetime import date

URL:str = 'https://randomuser.me/api/'
NUM_DISCOS = 8
TODAY = date.today()
n_left = 1

class Disco:
    name: str
    artist: str
    year: int
    price: float
    genre: str
    permited_genre = ["Pop", "Electro", "Reggaeton", "Rock", "Metal", "Death Metal", "Black Metal"]

    def __init__(self, _name, _artist, _year, _price, _genre):
        self.name = _name
        self.artist = _artist
        self.year = _year
        self.price = _price

        if _genre in Disco.permited_genre:      # solo deja crear discos de los generos permitidos
            self.genre = _genre
        else:
            raise ValueError("El género no es válido. Debe ser Pop, Electro, Reggaeton, Rock, Metal, Death Metal, Black Metal")

class Carrito:
    discos: []
    precio: float
    ahorro: float

    def __init__(self):
        self.discos = []
        self.precio = 0.00
        self.ahorro = 0.00
        
    def addCD(self, disco:Disco, discoutn:bool):
        self.discos.append(disco)
        self.precio = sum(disco.price for disco in self.discos)
        if(discoutn == True):
            self.ahorro = self.ahorro + disco.price*0.3


def random_name(url: str) -> str:
    respuesta = requests.get(url)
    status_code = respuesta.status_code
    datos = respuesta.json()
    if(status_code == 200):
        clase = datos['results'][0]
        nombre: str = clase["name"]["first"]
        apellido: str = clase["name"]["last"]
        return(f"{nombre}_{apellido}")
    else:
        return(f"Error: {status_code}")

def disco_random(num:int) -> Disco:
    cd_name = f"random_cd_{num}"
    cd_artist = random_name(URL)
    cd_year = random.randint(1940, TODAY.year)
    cd_price = float(random.randint(12,35))-0.01
    permited_genre = ["Pop", "Electro", "Reggaeton", "Rock", "Metal", "Death Metal", "Black Metal"]
    cd_genre = random.choices(permited_genre, k=1)[0]
    return(Disco(cd_name, cd_artist, cd_year, cd_price, cd_genre))

tienda = []
def catalogo():
    for disco in range(0, NUM_DISCOS):
        cd = disco_random(disco+1)
        tienda.append(cd)
        print(f"-{disco+1}. name: {cd.name}, artist: {cd.artist}, year: {cd.year}, genre: {cd.genre}, price: {cd.price}€")

def buy_cd(disco:Disco):
    if disco.genre == "Black Metal" or disco.genre == "Electro":
        carrito.addCD(disco, True)
    else:
        carrito.addCD(disco, False)



exit = False
print("Bienvenido a mi tienda de discos caballero")
print("Echa un vistazo, no te cortes!")
print("Por cierto, hay oferta el dia de hoy, 30% descuento los discos de genero Black Metal y Electro")
catalogo()
carrito = Carrito()

while(exit == False):
    
    keep_looking = input("Que quiere hacer? \n"
                         "Comprar 1(press '1')\n"
                         "Comprar 2(press '2')\n"
                         "Ver catalogo(press '3')\n"
                         "Irme(press '0'): ")
    if keep_looking == '0':
        exit = True
    elif(keep_looking == '1'):
        disco = tienda[int(input("Que disco quieres?(select number): ")) - 1]
        buy_cd(disco)
        print("Puedes seguir comprando si quieres")

    elif(keep_looking == '2'):
        disco1 = tienda[int(input("Que disco quieres?(select number): ")) - 1]
        disco2 = tienda[int(input("Que disco quieres?(select number): ")) - 1]
        buy_cd(disco1)
        buy_cd(disco2)
        print("Puedes seguir comprando si quieres")
    else:
        catalogo()





print("/////////////////////////////////////////////////////////////////////////")   
print("TICKET DE COMPRA")
print("CD Name    Price")
for disco in carrito.discos:
    print(f"-{disco.name}  {disco.price}€")
print("PRICE")
print(f'{"{:.2f}".format(carrito.precio)}€')
print("- Discount")
print("{:.2f}".format(carrito.ahorro))
print("TOTAL PRICE")
print(f'{"{:.2f}".format(carrito.precio-carrito.ahorro)}€')
print("/////////////////////////////////////////////////////////////////////////") 
        












