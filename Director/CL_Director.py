from Usuarios.CL_Usuario import Usuario
from Usuarios.utils.Rol import Roles
from datetime import datetime

class Director(Usuario):

    nom_usuario: str
    contraseña: str

    def __init__(self, dir_nombre: str,
                 dir_apellido: str,
                 dir_CURP: str,
                 dir_fecha_nacimiento: datetime,
                 dir_contraseña: str,
                 dir_nom_usuario: str
                 ):
        
        super().__init__(
            us_nombre=dir_nombre,
            us_apellido=dir_apellido,
            us_CURP=dir_CURP,
            us_fecha_nacimiento=dir_fecha_nacimiento,
            rol=Roles.DIRECTOR)
        
        self.nom_usuario = dir_nom_usuario
        self.contraseña = dir_contraseña
