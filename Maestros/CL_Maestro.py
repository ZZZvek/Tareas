from Usuario.CL_Usuario import Usuario
from Usuario.utils.Roles import Roles

class Maestro(Usuario):
    ma_ano_nacimiento: int
    ma_sueldo: float
    ma_rfc: str
    
    #Método constructor
    #Siempre que estamos dentro de una clase usamos self
    def __init__(self, ma_numero_control: str, ma_nombre: str, ma_apellido: str, sueldo: float, rfc: str, ano_nacimiento: str, contraseña: str):
        super().__init__(numero_control=ma_numero_control, nombre=ma_nombre, apellido=ma_apellido, contraseña=contraseña, rol=Roles.MAESTRO)
        self.ma_ano_nacimiento = ano_nacimiento
        self.ma_sueldo = sueldo
        self.ma_rfc = rfc
        
    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"""Número de control: {self.numero_control}
Nombre completo: {nombre_completo}
RFC: {self.ma_rfc}
Año de nacimiento: {self.ma_ano_nacimiento}
Sueldo: {self.ma_sueldo}
Rol: {self.rol.value}"""
        return info