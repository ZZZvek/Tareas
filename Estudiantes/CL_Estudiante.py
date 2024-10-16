from datetime import datetime
from Usuario.CL_Usuario import Usuario
from Usuario.utils.Roles import Roles

class Estudiante(Usuario):
    es_curp: str
    es_fecha_nacimiento: datetime
    
    #Método constructor
    #Siempre que estamos dentro de una clase usamos self
    def __init__(self, numero_control: str, nombre: str, apellido: str, curp: str, f_nacimiento: datetime, contraseña: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=Roles.ESTUDIANTE)
        self.es_curp = curp
        self.es_fecha_nacimiento = f_nacimiento 
        pass
    
    def mostrar_info_estudiante(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"""\nNúmero de control: {self.numero_control}
Nombre completo: {nombre_completo}
CURP: {self.es_curp}
Fecha de nacimiento: {self.es_fecha_nacimiento}
Rol: {self.rol.value}"""
        return info