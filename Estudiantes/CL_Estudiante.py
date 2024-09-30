from datetime import datetime

class Estudiante:
    es_numero_control: str
    es_nombre: str
    es_apellido: str
    es_curp: str
    es_fecha_nacimiento: datetime
    
    #Método constructor
    #Siempre que estamos dentro de una clase usamos self
    def __init__(self, numero_control: str,nombre: str, apellido: str, curp: str, f_nacimiento: datetime):
        self.es_numero_control = numero_control
        self.es_nombre = nombre
        self.es_apellido = apellido
        self.es_curp = curp
        self.es_fecha_nacimiento = f_nacimiento 
        pass
    
    def mostrar_info_estudiante(self):
        nombre_completo = f"{self.es_nombre} {self.es_apellido}"
        info = f"""Número de control: {self.es_numero_control}
Nombre completo: {nombre_completo}
CURP: {self.es_curp}
Fecha de nacimiento: {self.es_fecha_nacimiento}"""
        return info