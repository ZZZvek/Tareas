from Usuarios.CL_Usuario import Usuario
from Usuarios.utils.Rol import Roles
from datetime import datetime

class Visitante(Usuario):
    num_visitas: int = 0
    fecha_reg: datetime
    
    def __init__(self, 
                vi_nombre: str, 
                vi_apellido: str, 
                vi_fecha_nacimiento: datetime, 
                vi_CURP: str, 
                vi_num_visitas:int, 
                vi_fecha_reg:datetime
                ):
        
        super().__init__(
            us_nombre=vi_nombre, 
            us_apellido=vi_apellido, 
            us_fecha_nacimiento=vi_fecha_nacimiento, 
            us_CURP=vi_CURP,
            rol= Roles.VISITANTE)
    
        self.num_visitas=vi_num_visitas
        self.fecha_reg=vi_fecha_reg
        
    def incrementar_visitas(self):
        self.num_visitas += 1

    def mostrar_info_visitante(self):
        nombre_completo= f"{self.nombre} {self.apellido}"
        info_visitante = f"""
        Nombre: {nombre_completo}
        Fecha de nacimiento: {self.fecha_nacimiento}
        CURP: {self.CURP}
        Numero de visitas: {self.num_visitas}
        Fecha de registro: {self.fecha_reg}"""
        return info_visitante
    
    def descuento(self):
        descuento = 0.8 
        return descuento
            


    