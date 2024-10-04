from .utils.Roles import Roles

class Usuario:
    numero_control: str
    nombre: str
    apellido: str
    contraseña: str
    rol: Roles
    
    def __init__(self, numero_control: str, nombre: str, apellido: str, contraseña: str, rol: Roles):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña
        self.rol = rol
    pass