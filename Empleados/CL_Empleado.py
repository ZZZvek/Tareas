from Usuarios.CL_Usuario import Usuario
from datetime import datetime


class Empleado(Usuario):
    fecha_ingreso: datetime
    rfc: str
    salario: float
    horario: str

    def __init__(self, em_nombre: str, em_apellido: str, em_fecha_nacimiento: datetime, em_CURP: str,em_fecha_ingreso:datetime, em_rfc:str, em_salario:float, em_horario:str, rol):
        super().__init__(
            us_nombre=em_nombre, 
            us_apellido=em_apellido, 
            us_fecha_nacimiento=em_fecha_nacimiento, 
            us_CURP=em_CURP,
            rol=rol)
        
        self.fecha_ingreso=em_fecha_ingreso
        self.rfc=em_rfc
        self.salario=em_salario
        self.horario=em_horario
        

    def mostrar_info_empleado(self):
        nombre_completo= f"{self.nombre} {self.apellido}"
        info_empleado= f"""
Nombre: {nombre_completo} 
Fecha de nacimiento: {self.fecha_nacimiento} 
Fecha de ingreso: {self.fecha_ingreso} 
RFC: {self.rfc} 
Salario: {self.salario}
Horario: {self.horario}
CURP: {self.CURP}
    """
        return info_empleado