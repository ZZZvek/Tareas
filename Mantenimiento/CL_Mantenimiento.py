from datetime import datetime
from Empleados.CL_Empleado import Empleado
from Usuarios.utils.Rol import Roles

class Mantenimiento(Empleado):
    
    def __init__(self,
                 mant_nombre: str,
                 mant_apellido: str,
                 mant_CURP: str,
                 mant_fecha_nacimiento: datetime,
                 mant_fecha_ingreso: datetime,
                 mant_RFC: str,
                 mant_salario: str,
                 mant_horario: str
                 ):
        
        super().__init__(
            em_nombre=mant_nombre,
            em_apellido=mant_apellido,
            em_CURP=mant_CURP,
            em_fecha_nacimiento=mant_fecha_nacimiento,
            em_fecha_ingreso=mant_fecha_ingreso,
            em_rfc=mant_RFC,
            em_salario=mant_salario,
            em_horario=mant_horario,
            rol=Roles.MANTENIMIENTO)
        pass