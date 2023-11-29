# RETO 10

# Escribe un programa que guarde en una variable el siguiente contenido:
# {'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà',
# 'director':'Lucio Fulci', 'año':1981, 'país':'Itali

# sin terminar

contenido = "{'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà','director':'Lucio Fulci', 'año':1981, 'país':'Italia'}"

tamano = len(contenido)
variables = []
contiene = []
var = True
cont = False
var_esc = ""
cont_esc = ""

for letra in range(0, tamano):
    if(var == True):
     
        if(contenido[letra] == "{" or contenido[letra] == "}" or contenido[letra] == "'"):
            print("no hago nada aqui")
        elif(contenido[letra] == ":"):
            variables.append(var_esc)
            var = False
            cont = True
            var_esc = ""
        else:
            var_esc = var_esc + contenido[letra]

    elif(cont == True):
        if(contenido[letra] == "{" or contenido[letra] == "'"):
            print("no hago nada aqui")
        elif(contenido[letra] == "," or contenido[letra] == "}"):
            contiene.append(cont_esc)
            cont = False
            var = True
            cont_esc = ""
        else:
            cont_esc = cont_esc + contenido[letra]


print(variables)
print(contiene)
