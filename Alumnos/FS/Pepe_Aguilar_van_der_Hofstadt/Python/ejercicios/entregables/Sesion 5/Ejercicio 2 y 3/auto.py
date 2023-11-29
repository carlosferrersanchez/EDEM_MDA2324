## EJERCICIO 2

class Automovil:
    encendido:bool = False
    velocidad:float = 0
    deposito:float 
    gasolina:float
    gasto:float 
    marca:str
    matricula:str
    titular:str

    def __init__(self, _marca, _matricula, _titular, _deposito):
        self.marca = _marca
        self.matricula = _matricula
        self.titular = _titular
        self.deposito = _deposito
        self.gasolina = _deposito

    def out_of_gas(self)->bool:
        if(self.gasolina <= 0.5):
            print("¡SIN GASOLINA!")
            return True
        else:
            return False

    def arrancar(self):
        if(self.encendido == False):
            self.encendido = True
            print("El coche ha arrancado")
        else:
            if(self.out_of_gas(self) == False):
                self.gasolina -= 0.5
                print("Ya estaba encendido!")
    
    def acelerar(self, aceleracion, tiempo):
        velocidad_seg = self.velocidad/3.6
        if(self.encendido == True):
            if(self.out_of_gas() == False):
                self.velocidad = (aceleracion * tiempo + velocidad_seg)*3.6
                self.gasolina -= 2.5
                print(f'El coche va a una valocidad de {self.velocidad}km/h y le quedan {self.gasolina}L de gasolina')
    
    def frenar(self, deceleracion, tiempo):
        velocidad_seg = self.velocidad/3.6
        if(self.encendido == True):
            self.velocidad = (velocidad_seg - deceleracion * tiempo)*3.6
            print(f'El coche va a una valocidad de {self.velocidad}km/h y le quedan {self.gasolina}L de gasolina')
    
    def parar(self):
        self.velocidad = 0.0
        print(f'El coche está parado y le quedan {self.gasolina}L de gasolina')


#### EJERCICIO 3


class Coche(Automovil):
    n_plazas: int
    caballos: float

    def __init__(self, _marca, _matricula, _titular, _deposito, _n_plazas, _caballos):
        self.marca = _marca
        self.matricula = _matricula
        self.titular = _titular
        self.deposito = _deposito
        self.gasolina = _deposito
        self.n_plazas = _n_plazas
        self.caballos = _caballos

    def airbag(self):
        if(self.velocidad < 0):
            print("saltó el airbag")


class Moto(Automovil):
    casco: bool
    montana: bool

    def __init__(self, _marca, _matricula, _titular, _deposito, _casco, _montana):
        self.marca = _marca
        self.matricula = _matricula
        self.titular = _titular
        self.deposito = _deposito
        self.gasolina = _deposito
        self.casco = _casco
        self.montana = _montana

    def frenar(self, deceleracion, tiempo):
        velocidad_seg = self.velocidad/3.6
        if(self.encendido == True):
            self.velocidad = (velocidad_seg - deceleracion * tiempo)*3.6
            if(self.velocidad < 0):
                if(self.casco == True):
                    print("caiste, que susto")
                else:
                    print("NII NOO NII NOO NII NOO, estas muy grave de camino al hospital")
            else:        
                print(f'El coche va a una valocidad de {self.velocidad}km/h y le quedan {self.gasolina}L de gasolina')


class Camion(Automovil):
    mercancia_quimica: bool

    def __init__(self, _marca, _matricula, _titular, _deposito, _mercancia_quimica):
        self.marca = _marca
        self.matricula = _matricula
        self.titular = _titular
        self.deposito = _deposito
        self.gasolina = _deposito
        self.mercancia_quimica = _mercancia_quimica

    def frenar(self, deceleracion, tiempo):
        velocidad_seg = self.velocidad/3.6
        if(self.encendido == True):
            self.velocidad = (velocidad_seg - deceleracion * tiempo)*3.6
            if(self.velocidad < 0):
                print("BOOOOM")         
            else:        
                print(f'El coche va a una valocidad de {self.velocidad}km/h y le quedan {self.gasolina}L de gasolina')



