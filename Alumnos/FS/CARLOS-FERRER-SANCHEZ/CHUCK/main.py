import requests
from requests import Response

URL: str = 'https://api.chucknorris.io/jokes/random'

def guardar_palabras(texto, archivo):
    palabras = texto.split()
    palabras = set(map(str.lower, palabras))
    with open(archivo, 'w') as archivo_salida:  
        for palabra in palabras:
            archivo_salida.write(palabra + '\n')  

def funcion_chuck(veces, url, archivo):
    for bromas in range(veces):
        answer: Response = requests.get(url=URL) 
        data_json = answer.json()
        broma = data_json['value']
        guardar_palabras(broma, archivo)

funcion_chuck(2, URL, "results.txt")



