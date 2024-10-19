from Maestros.CL_Maestro import Maestro

class Materia:
    num_c_materia: str
    mt_nombre: str
    descripcion: str
    semestre: int
    creditos: int
    maestro: Maestro
    
    def __init__(self, num_materia:str, nombre:str, descripcion:str, semestre:int, creditos:int, maestro: Maestro):
        self.num_c_materia = num_materia
        self.mt_nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos
        self.maestro = maestro
        
    def mostrar_info_materia(self):
        info = f"""Número de control: {self.num_c_materia}
Nombre: {self.mt_nombre}
Descripción: {self.descripcion}
Semestre: {self.semestre}
Créditos: {self.creditos}
Mestro: {self.maestro.nombre}"""
        return info