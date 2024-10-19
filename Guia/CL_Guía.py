from datetime import datetime
from Empleados.CL_Empleado import Empleado
from Usuarios.utils.Rol import Roles

class Guia(Empleado):
    
    def __init__(self,
                 guia_nombre: str,
                 guia_apellido: str,
                 guia_CURP: str,
                 guia_fecha_nacimiento: datetime,
                 guia_fecha_ingreso: datetime,
                 guia_RFC: str,
                 guia_salario: float,
                 guia_horario: str
                 ):
        
        super().__init__(
            em_nombre=guia_nombre,
            em_apellido=guia_apellido,
            em_CURP=guia_CURP,
            em_fecha_nacimiento=guia_fecha_nacimiento,
            em_fecha_ingreso=guia_fecha_ingreso,
            em_rfc=guia_RFC,
            em_salario=guia_salario,
            em_horario=guia_horario,
            rol=Roles.GUIA
            )
        
        pass