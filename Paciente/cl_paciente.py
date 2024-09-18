import random



class Paciente:
    id: int
    nombre: str
    ano_nacimiento: int
    peso: float
    estatura: float
    direccion: str
    
    def __init__(self, nombre: str, ano_nacimiento: int, peso: float, estatura: float, direccion:str):
        self.id = random.randint(1,1000)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.peso = peso
        self.estatura = estatura
        self.direccion = direccion
        
    def mostrar_informacion(self):
        print("ID: ", self.id)
        print(f"Nombre: {self.nombre}")
        print("Año de nacimiento: ", self.ano_nacimiento)
        print("Estatura: ", self.estatura)
        print("Peso: ", self.peso)
        print("Dirección: ", self.direccion)