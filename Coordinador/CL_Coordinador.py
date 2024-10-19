from Usuario.CL_Usuario import Usuario
from Usuario.utils.Roles import Roles

class Coordinador(Usuario):
    coo_sueldo: float
    coo_rfc: str
    coo_años_ant: int
    
    def __init__(self, co_numero_control: str, co_nombre: str, co_apellido: str, co_sueldo: float, co_rfc: str, co_antiguedad: int, co_contraseña: str):
        super().__init__(numero_control=co_numero_control, nombre=co_nombre, apellido=co_apellido, contraseña=co_contraseña, rol=Roles.COORDINADOR)
        self.coo_sueldo = co_sueldo
        self.coo_rfc = co_rfc
        self.coo_años_ant = co_antiguedad