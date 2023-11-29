


class Alumno:
    nif: str
    nombre:str
    apellidos: str
    telefono: str
    email: str
    aprobado: bool

    def __init__(self, _nif, _nombre, _apellidos, _telefono, _email, _aprobado):
        self.nif = _nif
        self.nombre = _nombre
        self.apellidos = _apellidos
        self.telefono = _telefono
        self.email = _email
        self.aprobado = _aprobado


salir = False
lista_alumnos = []

while(salir == False):

    opcion = input("(1) Añadir alumno\n"
                   "(2) Eliminar alumno\n"
                   "(3) Atualizar alumno\n"
                   "(4) Mostrar alumno (por NIF)\n"
                   "(5) Mostrar alumno (por mail)\n"
                   "(6) Mostrar todos los alumnos\n"
                   "(7) Aprobar alumno\n"
                   "(8) Suspender alumno\n"
                   "(9) Mostrar alumnos aprobados\n"
                   "(10) Mostrar alumnos suspensos\n"
                   "(X) Salir\n")

    if(opcion == '1'):      # Se podria comprobar que los valores son correctos pj no meten un numero en vez de string 
        print("Introduce el alumno.")

        nif = input("Introduce el NIF del alumno: ")
        nombre = input("Introduce el nombre del alumno: ")
        apellidos = input("Introduce los apellidos del alumno: ")
        telf = input("Introduce el telefono del alumno: ")
        mail = input("Introduce el email del alumno: ")
        aprueba = input("Introduce SI o NO si ha aprobado o no el alumno: ")

        if(aprueba == 'SI'):
            aprobado = True
        else:
            aprobado = False

        lista_alumnos.append(Alumno(nif, nombre, apellidos, telf, mail, aprobado))
    
    elif(opcion == '2'):
        print("Elimina un alumno.")
        nif = input("Introduce el NIF del alumno que quieras elimianr: ")

        for alumno in lista_alumnos:    # en caso de que haya dos alumnos con mismo nif(no deberia) solo eliminará el primero 
            if(alumno.nif == nif):
               lista_alumnos.remove(alumno)
               break 

    elif(opcion == '3'):
        print("Actualiza un alumno")
        nif = input("Introduce el NIF del alumno que quieras actualizar: ")

        for alumno in lista_alumnos:    # en caso de que haya dos alumnos con mismo nif(no deberia) solo eliminará el primero 
            if(alumno.nif == nif):
                actualizado = False
                while(actualizado == False):    # No perimte actualizar NIF ni Aprobado (hay otra funcion para eso)
                    dato = input("Selecciona el campo a actualizar: \n(1) Nombre\n(2) Apellidos\n(3) Telefono\n(4) Email\n(5) Fin de actualizacion\n")
                    if(dato == '1'):
                        nombre = input("Introduce el nuevo nombre: ")
                        alumno.nombre = nombre
                    elif(dato == '2'):
                        ap = input("Introduce los nuevos apeliidos: ")
                        alumno.apellidos = ap
                    elif(dato == '3'):
                        tel = input("Introduce el nuevo telefono: ")
                        alumno.telefono = tel
                    elif(dato == '4'):
                        mail = input("Introduce el nuevo email: ")
                        alumno.email = mail
                    else:
                        actualizado = True

    elif(opcion == '4'):
        print("Muestra a un alumno")
        nif = input("Introduce el NIF del alumno que quieres ver: ")

        for alumno in lista_alumnos:
            if(alumno.nif == nif):
                print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, Telefono: {alumno.telefono}, email: {alumno.email}, Aprobado: {alumno.aprobado}")

    elif(opcion == '5'):
        print("Muestra a un alumno")
        email = input("Introduce el email del alumno que quieres ver: ")

        for alumno in lista_alumnos:
            if(alumno.email == email):
                print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, Telefono: {alumno.telefono}, email: {alumno.email}, Aprobado: {alumno.aprobado}")

    elif(opcion == '6'):
        for alumno in lista_alumnos:
            print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, Telefono: {alumno.telefono}, email: {alumno.email}, Aprobado: {alumno.aprobado}")
        
    elif(opcion == '7'):
        print("Aprueba al alumno")
        nif = input("Introduce el NIF del alumno que quieres aprobar: ")

        for alumno in lista_alumnos:
            if(alumno.nif == nif):
                alumno.aprobado = True

    elif(opcion == '8'):
        print("Suspende al alumno")
        nif = input("Introduce el NIF del alumno que quieres suspender: ")

        for alumno in lista_alumnos:
            if(alumno.nif == nif):
                alumno.aprobado = False

    elif(opcion == '9'):
        print("Alumnos aprobados")

        for alumno in lista_alumnos:
            if(alumno.aprobado == True):
                print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, Telefono: {alumno.telefono}, email: {alumno.email}, Aprobado: {alumno.aprobado}")

    elif(opcion == '10'):
        print("Alumnos Suspensos")

        for alumno in lista_alumnos:
            if(alumno.aprobado == False):
                print(f"NIF: {alumno.nif}, Nombre: {alumno.nombre}, Apellidos: {alumno.apellidos}, Telefono: {alumno.telefono}, email: {alumno.email}, Aprobado: {alumno.aprobado}")

    elif(opcion == 'X'):
        salir = True



