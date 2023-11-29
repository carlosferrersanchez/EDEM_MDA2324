import requests

def random_user_generation(url: str):
    respuesta = requests.get(url)
    status_code = respuesta.status_code
    datos = respuesta.json()
    if(status_code == 200):
        clase = datos['results'][0]
        nombre: str = clase["name"]["first"]
        apellido: str = clase["name"]["last"]
        edad: str = clase["dob"]["age"]
        genero: str = clase["gender"]
        print(f'{nombre} {apellido}, {edad} years, {genero}')
    else:
        print(f"Error: {status_code}")


URLU:str = 'https://randomuser.me/api/'


random_user_generation(URLU)