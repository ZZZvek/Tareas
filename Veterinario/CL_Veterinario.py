from datetime import datetime
from Empleados.CL_Empleado import Empleado
from Usuarios.utils.Rol import Roles

class Veterinario(Empleado):
    
    def __init__(self,
                 vet_nombre: str,
                 vet_apellido: str,
                 vet_CURP: str,
                 vet_fecha_nacimiento: datetime,
                 vet_fecha_ingreso: datetime,
                 vet_RFC: str,
                 vet_salario: float,
                 vet_horario: str
                 ):
        
        super().__init__(
            em_nombre=vet_nombre,
            em_apellido=vet_apellido,
            em_CURP=vet_CURP,
            em_fecha_nacimiento=vet_fecha_nacimiento,
            em_fecha_ingreso=vet_fecha_ingreso,
            em_rfc=vet_RFC,
            em_salario=vet_salario,
            em_horario=vet_horario,
            rol=Roles.VETERINARIO
            )
        


    