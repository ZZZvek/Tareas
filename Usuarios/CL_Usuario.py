from .utils.Rol import Roles
from datetime import datetime

class Usuario:
    nombre: str
    apellido: str
    fecha_nacimiento: datetime
    CURP: str
    rol:Roles
    
    def __init__(self, us_nombre: str, us_apellido: str, us_fecha_nacimiento: datetime, us_CURP: str, rol: Roles):
        self.nombre = us_nombre
        self.apellido = us_apellido
        self.fecha_nacimiento = us_fecha_nacimiento
        self.CURP = us_CURP
        self.rol= rol 
        pass