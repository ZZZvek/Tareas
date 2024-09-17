import random

class Paciente:
    id = 0
    nombre = ""
    ano_nacimiento = 0
    peso = 0
    estatura = 0
    direccion = ""
    
    def __init__(self, nombre, ano_nacimiento, peso, estatura, direccion):
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