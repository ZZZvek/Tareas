import random

class Medico:
    id = 0
    nombre = ""
    ano_nacimiento = 0
    rfc = 0
    direccion = ""
    
    def __init__(self, nombre, ano_nacimiento,rfc, direccion):
        self.id = random.randint(1,1000)
        self.nombre = nombre
        self.ano_nacimiento = ano_nacimiento
        self.rfc = rfc
        self.direccion = direccion
        
    def mostrar_informacion(self):
        print("Id: ", self.id)
        print(f"Nombre: {self.nombre}") 
        print(f"Año de nacimiento: {self.ano_nacimiento}")
        print(f"RFC: {self.rfc}")
        print(f"Direccion: {self.direccion}\n")
        
    # @property
    # def id(self):
    #     return self.id
    # @property
    # def nombre(self):
    #     return self.nombre
    # @property
    # def ano_nacimiento(self):
    #     return self.ano_nacimiento
    # @property
    # def rfc(self):
    #     return self.rfc
    # @property
    # def direccion(self):
    #     return self.direccion