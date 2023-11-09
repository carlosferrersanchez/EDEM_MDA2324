import requests
from requests.models import Response
URL: str = 'https://api.chucknorris.io/jokes/random'

palabras_min = []
joke_chuck = []
def funcion_chuck(veces, url):
    f = open("results.txt", "w")
    for bromas in range(veces):
        answer: Response = requests.get(url=URL) 
        data_json = answer.json()
        broma = data_json['value']
        joke_chuck.append(broma)
        for words in joke_chuck:
            minusculas = words.lower()
            palabras_min.append(minusculas)
        f.write(f"{palabras_min}\n")

funcion_chuck(10, URL)
print(palabras_min)



